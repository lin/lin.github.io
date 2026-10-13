### React State

```js
const StateTestComponent = () => {
    const dateWithoutState = new Date()
    
    const [dateWithState, setDateWithState] = useState(new Date())
    const [count, setCount] = useState(0)

    return (
        <div className="flex flex-row text-2xl h-screen">
            <div id="left-half" className="bg-red-300 w-1/4">
                {dateWithoutState.toISOString()}
            </div>
            <div id="right-half" className="bg-blue-300 w-1/4">
                <div>{dateWithState.toISOString()}</div>
                <button onClick={() => setDateWithState(new Date())}>Update Time</button>
            </div>
            <div id="right-half" className="bg-purple-300 w-2/4">
                <div>{count}</div>
                <button onClick={() => setCount(count + 1)}>Update Count</button>
            </div>
        </div>
    )
}
```