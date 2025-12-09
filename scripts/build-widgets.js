#!/usr/bin/env node

/**
 * Build script for React widgets
 * Transpiles ES6 modules in static/js/widgets/ to browser-compatible bundles
 */

const esbuild = require('esbuild');
const fs = require('fs');
const path = require('path');

const widgetsDir = path.join(__dirname, '../static/js/widgets');
const outputDir = path.join(__dirname, '../static/js/compiled');

// Ensure output directory exists
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

// Get all .js files in widgets directory
const widgetFiles = fs.readdirSync(widgetsDir)
  .filter(file => file.endsWith('.js'))
  .map(file => path.join(widgetsDir, file));

const isWatch = process.argv.includes('--watch');

const buildOptions = {
  bundle: true,
  format: 'iife',
  loader: { '.js': 'jsx' },
  // Map React imports to global variables using esbuild's define
  define: {
    'process.env.NODE_ENV': '"production"'
  },
  // Don't bundle React - it's loaded globally
  external: [],
  // Replace React imports with window globals
  plugins: [{
    name: 'replace-react-imports',
    setup(build) {
      // Intercept react imports and return empty - we'll use globals
      build.onResolve({ filter: /^react$/ }, args => {
        return { path: args.path, namespace: 'react-ns' }
      });
      build.onResolve({ filter: /^react-dom$/ }, args => {
        return { path: args.path, namespace: 'react-dom-ns' }
      });
      
      build.onLoad({ filter: /.*/, namespace: 'react-ns' }, () => {
        return {
          contents: 'module.exports = window.React',
          loader: 'js'
        }
      });
      
      build.onLoad({ filter: /.*/, namespace: 'react-dom-ns' }, () => {
        return {
          contents: 'module.exports = window.ReactDOM',
          loader: 'js'
        }
      });
    }
  }]
};

async function build() {
  try {
    console.log('Building React widgets...');
    
    // Build each widget separately to get proper names
    for (const widgetFile of widgetFiles) {
      const componentName = path.basename(widgetFile, '.js');
      
      await esbuild.build({
        ...buildOptions,
        entryPoints: [widgetFile],
        outfile: path.join(outputDir, `${componentName}.js`),
        globalName: `__Widget_${componentName}__`,
        footer: {
          js: `
// Auto-register the widget
if (typeof __Widget_${componentName}__ !== 'undefined' && __Widget_${componentName}__.default) {
  window.registerWidget && window.registerWidget('${componentName}', __Widget_${componentName}__.default);
}
          `.trim()
        }
      });
      
      console.log(`✓ Built ${componentName}.js`);
    }
    
    console.log('✓ All widgets built successfully!');
  } catch (error) {
    console.error('Build failed:', error);
    process.exit(1);
  }
}

if (isWatch) {
  console.log('Watching for changes...');
  
  esbuild.context({
    ...buildOptions,
    plugins: [{
      name: 'rebuild-notify',
      setup(build) {
        build.onEnd(result => {
          if (result.errors.length === 0) {
            console.log('✓ Widgets rebuilt');
          }
        });
      }
    }]
  }).then(ctx => {
    ctx.watch();
  });
} else {
  build();
}
