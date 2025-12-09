/**
 * React Widget System for Hugo
 * This script manages the lifecycle of React components embedded in Hugo pages
 */

// Widget registry - stores all available widget components
window.WidgetRegistry = window.WidgetRegistry || {};

/**
 * Register a new widget component
 * @param {string} name - Component name
 * @param {Function} component - React component
 */
window.registerWidget = function(name, component) {
  window.WidgetRegistry[name] = component;
  console.log(`Widget registered: ${name}`);
};

/**
 * Initialize and render all queued widgets
 */
function initializeWidgets() {
  if (!window.React || !window.ReactDOM) {
    console.error('React or ReactDOM not loaded');
    return;
  }

  const widgets = window.reactWidgets || [];
  
  widgets.forEach(widget => {
    const { id, component, props } = widget;
    const container = document.getElementById(id);
    
    if (!container) {
      console.warn(`Container not found for widget: ${id}`);
      return;
    }

    const Component = window.WidgetRegistry[component];
    
    if (!Component) {
      console.error(`Widget component not found: ${component}`);
      container.innerHTML = `<div style="color: red; padding: 10px; border: 1px solid red;">
        Widget "${component}" not found. Available widgets: ${Object.keys(window.WidgetRegistry).join(', ')}
      </div>`;
      return;
    }

    try {
      // Create root and render component
      const root = ReactDOM.createRoot(container);
      root.render(React.createElement(Component, props));
      console.log(`Widget rendered: ${component} (${id})`);
    } catch (error) {
      console.error(`Error rendering widget ${component}:`, error);
      container.innerHTML = `<div style="color: red; padding: 10px; border: 1px solid red;">
        Error rendering widget "${component}": ${error.message}
      </div>`;
    }
  });
}

// Initialize widgets when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeWidgets);
} else {
  initializeWidgets();
}
