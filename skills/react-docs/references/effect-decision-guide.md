# Effect Decision Guide

Use this guide when a component contains `useEffect` and you need to decide whether it should exist at all.

## Quick test

Ask: what external system is this synchronizing with?

- If the answer is "none", the Effect is probably unnecessary.
- If the answer is DOM API, network state, subscription, timer, third-party widget, browser API, or another system outside React, the Effect may be valid.

## Replace unnecessary Effects with these patterns

### Derive during render

Use when state is only a transformation of props or other state.

```tsx
const fullName = `${firstName} ${lastName}`
const visibleItems = items.filter((item) => item.active)
const selectedItem = items.find((item) => item.id === selectedId) ?? null
```

Common smell:

```tsx
useEffect(() => {
  setVisibleItems(items.filter((item) => item.active))
}, [items])
```

### Move into the event handler

Use when logic exists because the user clicked, submitted, dragged, or otherwise triggered a specific interaction.

```tsx
const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
  event.preventDefault()
  post("/api/register", { firstName, lastName })
}
```

Common smell:

```tsx
useEffect(() => {
  if (jsonToSubmit) {
    post("/api/register", jsonToSubmit)
  }
}, [jsonToSubmit])
```

### Reset with a key

Use when a prop change should recreate a whole subtree and all of its local state.

```tsx
return <ProfileForm key={userId} userId={userId} />
```

### Adjust during render only as a fallback

Use sparingly when some state must be adjusted from a changed prop and neither derivation nor keyed reset fits.

```tsx
const [prevItems, setPrevItems] = useState(items)
if (items !== prevItems) {
  setPrevItems(items)
  setSelection(null)
}
```

Prefer deriving state away entirely when possible.

### Lift state or control the child

Use when parent and child are trying to keep mirrored state in sync.

```tsx
const [isOn, setIsOn] = useState(false)
return <Toggle isOn={isOn} onChange={setIsOn} />
```

### Use `useSyncExternalStore`

Use when subscribing to a mutable source outside React.

```tsx
return useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot)
```

## Valid Effect categories

- subscribe and unsubscribe from an external source
- connect and disconnect to a third-party widget or service
- fetch data that must stay synchronized with visible state
- start and stop timers tied to visibility or dependencies
- imperatively read or write browser APIs that cannot happen during render

## Fetching guidance

Fetching can live in an Effect when the goal is to synchronize UI with network data for the current visible inputs. Add cleanup to avoid stale responses winning the race.

```tsx
useEffect(() => {
  let ignore = false

  fetchResults(query, page).then((json) => {
    if (!ignore) {
      setResults(json)
    }
  })

  return () => {
    ignore = true
  }
}, [query, page])
```

Prefer framework-native data fetching when available.

## Review checklist

- Does this Effect synchronize with something outside React?
- Can the value be derived during render instead?
- Can the work happen inside the triggering event handler instead?
- Can a keyed subtree reset replace manual reset logic?
- Is the component mirroring parent or child state that should be lifted?
- If the Effect remains, is every dependency truly required?
