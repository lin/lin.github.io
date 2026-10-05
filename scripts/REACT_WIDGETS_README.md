# React Widgets in Hugo

This Hugo site supports embedding React components using a custom widget system with ES6 module syntax.

## Setup

### 1. Install Dependencies

```bash
npm install
```

This installs:
- `esbuild` - Fast JavaScript bundler
- `react` & `react-dom` - React libraries (for type checking)

### 2. Build Widgets

```bash
npm run build:widgets
```

This transpiles all `.js` files in `static/js/widgets/` to browser-compatible bundles in `static/js/compiled/`.

### 3. Development Mode

```bash
npm run dev
```

This runs both:
- Widget builder in watch mode (auto-rebuilds on changes)
- Hugo development server

## Creating a Widget

### 1. Write Your Component

Create a file in `static/js/widgets/YourWidget.js`:

```javascript
import React, { useState } from 'react';

const YourWidget = ({ title = "Default Title" }) => {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <h2>{title}</h2>
      <button onClick={() => setCount(count + 1)}>
        Count: {count}
      </button>
    </div>
  );
};

export default YourWidget;
```

**Key points:**
- Use ES6 `import`/`export` syntax
- Import React hooks normally
- Export your component as `default`
- Component name should match filename

### 2. Build the Widget

```bash
npm run build:widgets
```

This creates `static/js/compiled/YourWidget.js`.

### 3. Use in Markdown

In any markdown file (e.g., `content/posts/my-post.md`):

```markdown
---
title: "My Post"
---

Here's my widget:

{{</* react-widget component="YourWidget" title="Hello World" */>}}
```

**Passing props:**
- All shortcode parameters (except `component`) are passed as props
- Use standard Hugo shortcode syntax
- Props are automatically JSON-encoded

## How It Works

### Architecture

1. **Widget Files** (`static/js/widgets/*.js`)
   - Written with ES6 modules
   - Use React hooks and modern syntax
   - One component per file

2. **Build Script** (`scripts/build-widgets.js`)
   - Uses esbuild to bundle each widget
   - Maps React imports to global `window.React`
   - Auto-registers components in `window.WidgetRegistry`
   - Outputs to `static/js/compiled/`

3. **Widget Registry** (`static/js/react-widgets.js`)
   - Manages component registration
   - Handles rendering lifecycle
   - Provides error handling

4. **Hugo Shortcode** (`layouts/shortcodes/react-widget.html`)
   - Creates container div with unique ID
   - Queues widget for initialization
   - Passes props as JSON

5. **Loader Partial** (`layouts/partials/react-widgets-loader.html`)
   - Auto-detects widgets used on page
   - Loads React from CDN
   - Loads only required widget bundles

### Build Process

```
static/js/widgets/GMMVisualizer.js
  ↓ (esbuild)
static/js/compiled/GMMVisualizer.js
  ↓ (Hugo)
public/js/compiled/GMMVisualizer.js
```

### Runtime Process

```
1. Page loads
2. React CDN scripts load
3. react-widgets.js loads (registry system)
4. Widget bundles load (auto-registered)
5. DOMContentLoaded fires
6. Widgets render into containers
```

## Example: GMMVisualizer

Your existing `GMMVisualizer.js` works perfectly with this system:

```javascript
import React, { useState, useEffect, useRef, useCallback } from 'react';

const GMMVisualizer = () => {
  // ... your implementation
  return <div>...</div>;
};

export default GMMVisualizer;
```

Use it in markdown:

```markdown
{{</* react-widget component="GMMVisualizer" */>}}
```

## Troubleshooting

### Widget not rendering?

1. Check browser console for errors
2. Verify widget was built: `ls static/js/compiled/`
3. Check component name matches filename
4. Ensure `export default` is present

### Build errors?

1. Check for syntax errors in widget file
2. Ensure all imports are valid
3. Run `npm run build:widgets` to see detailed errors

### Props not working?

1. Props are passed as strings by default
2. Hugo's `jsonify` handles complex types
3. Check browser console for prop values

## Advanced Usage

### Custom Props

```markdown
{{</* react-widget 
  component="MyWidget" 
  title="Hello"
  count="42"
  enabled="true"
*/>}}
```

### Multiple Widgets

```markdown
{{</* react-widget component="Counter" */>}}

Some text here...

{{</* react-widget component="GMMVisualizer" */>}}
```

### Widget Communication

Widgets are isolated by default. For communication:
- Use URL parameters
- Use localStorage/sessionStorage
- Implement a global event bus

## Performance

- React loaded from CDN (cached across sites)
- Only widgets used on page are loaded
- Widgets are bundled (no runtime transpilation)
- Minimal overhead (~50KB for React + ReactDOM)

## Deployment

### GitHub Pages / Netlify

1. Add build command: `npm run build`
2. Commit `static/js/compiled/` or build on deploy
3. Ensure Node.js is available in build environment

### Manual Deployment

```bash
npm run build:widgets
hugo
# Deploy public/ directory
```
