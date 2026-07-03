---
title: 'Why Does Modifying a Copy Sometimes Change the Original?'
pubDate: 2026-07-03 17:34:49
description: "We're used to thinking of a copy as a completely independent duplicate. The confusion comes from the fact that Python supports more than one kind of copying."
tags: ["python", "copy", "deepcopy"]
---
> We assume you already know how to write simple Python programs and understand basic syntax (if, for, functions, lists). Here, we're not discussing how to use the language, but why it works the way it does.

Try to guess what this code prints.

```python
numbers = [[1, 2], [3, 4]]

copy = numbers.copy()

copy[0].append(99)

print(numbers)
```

If you take the word *copy* literally, the answer seems obvious.

We modified the copy.

So the original should stay unchanged.

Many people expect:

```python
[[1, 2], [3, 4]]
```

But Python prints:

```python
[[1, 2, 99], [3, 4]]
```

That seems rather strange.

We modified the copy, yet the original changed too.

Does that mean `copy()` is broken?

---

Not at all.

`copy()` is working exactly as intended.

The confusion comes from the fact that Python supports more than one kind of copying.

We're used to thinking of a copy as a completely independent duplicate.

But `copy()` doesn't work that way.

It creates a new list.

It does **not** copy the objects stored inside that list.

Let's see what actually happens.

After executing:

```python
numbers = [[1, 2], [3, 4]]
```

Python creates three objects.

Two inner lists:

```text
[1, 2]

[3, 4]
```

and one outer list that refers to them.

Visually:

```text
numbers
    │
    ▼
┌──────────────┐
│  •      •    │
└──┼──────┼────┘
   │      │
   ▼      ▼
[1, 2]  [3, 4]
```

Now we execute:

```python
copy = numbers.copy()
```

Python creates a new outer list.

However, the elements of that list still refer to the very same inner lists.

Now the picture looks like this:

```text
numbers ─┐
          │
          ▼
     ┌──────────────┐
     │  •      •    │
     └──┼──────┼────┘
        │      │
        ▼      ▼
      [1,2]  [3,4]
        ▲      ▲
        │      │
     ┌──┼──────┼────┐
     │  •      •    │
     └──────────────┘
          ▲
          │
        copy
```

Notice what changed.

There are now two outer lists.

But there are still only two inner lists.

That's why this line:

```python
copy[0].append(99)
```

doesn't really modify "the copy."

It modifies one of the shared inner lists.

Since both outer lists refer to that same object, the change becomes visible through both of them.

---

At this point, you might wonder:

If `copy()` doesn't make a completely independent copy, why does it exist at all?

The answer depends on what your program actually needs.

Very often, creating a new container is enough.

For example:

```python
numbers = [1, 2, 3]

copy = numbers.copy()
```

Here, the elements are numbers.

And numbers are immutable.

So a shallow copy is usually all you need.

The interesting cases begin when a collection contains other mutable objects.

For example:

- lists;
- dictionaries;
- sets.

In these situations, a shallow copy is no longer sufficient.

---

Fortunately, Python also provides a way to create a completely independent copy.

The `copy` module includes a function called `deepcopy()`.

```python
from copy import deepcopy

numbers = [[1, 2], [3, 4]]

copy = deepcopy(numbers)

copy[0].append(99)

print(numbers)
```

Now the output is:

```python
[[1, 2], [3, 4]]
```

Why?

Because `deepcopy()` doesn't stop at the outer list.

It recursively creates copies of every nested object.

After a deep copy, the two collections no longer share any of their inner lists.

---

We can now summarize the difference.

A **shallow copy** creates a new container, but reuses the objects stored inside it.

A **deep copy** recursively creates new objects throughout the entire object hierarchy.

---

Once again, nothing magical is happening.

There are objects.

There are references between those objects.

`copy()` copies the references.

`deepcopy()` creates new objects instead.

---

By now, we've built a pretty solid understanding of how Python objects are created, modified, and copied.

But there's still one important question left.

Sometimes it seems that an object is no longer needed.

For example:

```python
numbers = [1, 2, 3]

del numbers
```

What happens to the object itself?

Does it disappear immediately?

Or does Python keep it around for a while?

That's exactly what we'll explore in the next article.
