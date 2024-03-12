```js
React.createElement(
  'h1',      // type
  {},        // props
  'Hello, React!' // children
);
```

## Generate HTML String

## Re-render when state change.

## Use Effect

```js
useEffect(() => {
  // Code to run on mount and update (componentDidMount and componentDidUpdate)

  return () => {
    // Cleanup code (componentWillUnmount)
  };
}, [someValue]); // Run again only if `someValue` changes
```