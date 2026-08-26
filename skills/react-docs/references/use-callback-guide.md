# useCallback Guide

Use this guide when deciding whether `useCallback` helps or just adds noise.

## Default stance

Do not add `useCallback` by default. Keep it when there is a concrete optimization or dependency reason.

## Good reasons to keep `useCallback`

### Stable prop for a memoized child

Keep it when a slow child wrapped in `memo` depends on stable function identity.

```tsx
const handleSubmit = useCallback((orderDetails: OrderDetails) => {
  post(`/product/${productId}/buy`, { referrer, orderDetails })
}, [productId, referrer])

return <ShippingForm onSubmit={handleSubmit} />
```

### Stable function returned from a custom Hook

Keep it when consumers of a Hook may depend on stable callback identity.

```tsx
const navigate = useCallback((url: string) => {
  dispatch({ type: "navigate", url })
}, [dispatch])
```

### Temporary bridge while removing an Effect dependency is not yet practical

This is acceptable, but check whether moving the function inside the Effect is cleaner.

## Common ways to avoid `useCallback`

### Move the helper inside the Effect

Prefer this when the function is only used by that Effect.

```tsx
useEffect(() => {
  const options = {
    serverUrl: "https://localhost:1234",
    roomId,
  }

  const connection = createConnection(options)
  connection.connect()

  return () => {
    connection.disconnect()
  }
}, [roomId])
```

### Use an updater function

Prefer this when the callback only reads state to compute next state.

```tsx
const handleAddTodo = useCallback((text: string) => {
  const newTodo = { id: nextId++, text }
  setTodos((todos) => [...todos, newTodo])
}, [])
```

### Remove the optimization entirely

If the child is not slow or not memoized, the stable callback often does nothing useful.

## React Compiler note

React Compiler can automatically memoize functions and values, which reduces the need for manual `useCallback`. In compiler-enabled codebases, prefer the clearest implementation unless profiling shows a real need.

## Review checklist

- Is this callback required for correctness? If yes, there is probably a deeper design issue.
- Is it feeding a memoized child or another Hook dependency that benefits from stability?
- Can the function move inside the Effect that uses it?
- Can an updater function remove a state dependency?
- Does React Compiler make this hook unnecessary in this codebase?
