---
title: "Why You Shouldn't Use `def func(items=[])`"
pubDate: 2026-06-27 18:31:49
description: "To understand what's going on, it's enough to recall what we discussed in previous articles. First, variables don't store objects - they only reference them. Second, a list is a mutable object."
tags: ["python", "list", "function", "default", "mutable", "arguments"]
---
> We assume you already know how to write simple Python programs and understand basic syntax (if, for, functions, lists). Here, we're not discussing how to use the language, but why it works the way it does.

Try to guess what this code prints:

```python
def add(item, items=[]):
    items.append(item)
    return items

print(add(1))
print(add(2))
print(add(3))
```

If you've never encountered this behavior before, you might expect something like:

```python
[1]
[2]
[3]
```

Each function call looks independent from the previous one.

However, Python produces a very different result:

```python
[1]
[1, 2]
[1, 2, 3]
```

It looks as if the list somehow "remembers" previous function calls.

But why does this happen?

---

If you look at this example in isolation, it might seem like Python functions have some kind of hidden memory.

In reality, there is nothing magical going on.

To understand this behavior, we only need to recall two ideas from previous articles:

- variables don't store objects, they refer to them;
- lists are mutable objects.

Together, these two facts fully explain what's happening.

---

When Python encounters a function definition:

```python
def add(item, items=[]):
    ...
```

the default list is created **exactly once**.

Not on every function call.

Not each time `add()` is executed.

But at the moment the function is defined.

We can think of it like this:

```text
add
 │
 └────► items ───► []
```

The function parameter `items` is bound to a single list object.

Now the first call happens:

```python
add(1)
```

Since no second argument is provided, Python uses the existing default list.

After `append()`, it looks like this:

```text
items ───► [1]
```

The function finishes execution.

But the list does not disappear.

It continues to exist.

---

Now the second call happens:

```python
add(2)
```

One might expect Python to create a new empty list.

But it doesn't.

The same object is reused.

Now the list becomes:

```text
items ───► [1, 2]
```

The third call behaves the same way.

The same list keeps being modified:

```text
items ───► [1, 2, 3]
```

This is why each call appears to "remember" previous results.

---

It's important to notice that the issue is not with functions themselves.

If we write the same logic without a function, nothing surprising happens:

```python
items = []

items.append(1)
items.append(2)
items.append(3)

print(items)
```

The result is:

```python
[1, 2, 3]
```

We already know why this happens.

A list is a mutable object.

Each `append()` modifies the same object instead of creating a new one.

The function behaves exactly the same way.

The only difference is that the list was created earlier than many people expect.

---

So how do we write this correctly?

Python has a widely accepted pattern for this case.

Instead of using a mutable default value, we use `None`:

```python
def add(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

Now each call without an explicit list creates a new one.

The behavior becomes predictable:

```python
print(add(1))
print(add(2))
print(add(3))
```

```python
[1]
[2]
[3]
```

---

You might wonder why Python behaves this way at all.

Why not create a new list automatically for each function call?

The reason is simple: default argument values are objects like everything else in Python.

They are created once at function definition time and then reused.

This makes the behavior consistent and efficient.

For immutable objects like numbers or strings, this behavior is usually invisible.

But once a mutable object like a list, dictionary, or set is used as a default value, the effect becomes observable.

---

From everything we've learned so far, nothing new is actually happening here.

There is an object.

There is a reference to that object.

The object is mutable.

So every function call modifies the same shared list.

This is why experienced Python developers almost never use mutable objects as default argument values.

---

At this point, we know enough to move one step further.

We've repeatedly said that lists can be modified in place.

But is that always true?

For example, what happens here?

```python
numbers = [1, 2]

numbers += [3]
```

Is the existing list modified, or is a new list created?

And what if we replace the list with a number?

On the surface, the operation looks the same - but the behavior can be very different.

That's exactly what we'll explore in the next article.
