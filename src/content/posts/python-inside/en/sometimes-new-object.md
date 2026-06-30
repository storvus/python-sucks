---
title: 'Why Does `+=` Sometimes Create a New Object and Sometimes Not?'
pubDate: 2026-06-30 18:20:34
description: "Many people expect `+=` to simply change a variable. But if you inspect the object with `id()`, you'll sometimes discover that it's actually a different object. Why does `+=` create a new object in some cases but not others?"
tags: ["python", "types", "immutable", "mutable"]
---

> This article assumes you're already comfortable writing simple Python programs and know the basics (`if`, `for`, functions, and lists). Here we're not learning **how** to use Python—we're learning **why** it behaves the way it does.

Try to guess what this code prints.

```python
x = 10

print(id(x))

x += 5

print(id(x))
```

Many people expect `+=` to simply change the value of the variable.

But if you look at the result of `id()`, you'll find that it's now a different object.

It seems as though `+=` created a brand-new object.

Now consider a very similar example.

```python
numbers = [1, 2]

print(id(numbers))

numbers += [3]

print(id(numbers))
```

This time, `id()` stays exactly the same.

Now the behavior is the complete opposite.

In one case, a new object appears.

In the other, the existing object is reused.

Why?

---

If you've followed the previous articles, the answer is already within reach.

We know two important things:

- a name doesn't store an object—it simply refers to one;
- Python has both mutable and immutable objects.

The second point turns out to be the key.

---

Let's start with a number.

```python
x = 10
```

The name `x` refers to the object `10`.

```text
x ───► 10
```

Now we execute:

```python
x += 5
```

At first glance, it looks like the number itself has changed.

But numbers are immutable objects.

We've already learned that immutable objects cannot be modified.

So Python does something else instead.

First, it computes:

```python
10 + 5
```

Then it creates a new object whose value is `15`.

Finally, the name `x` is rebound to that object.

Conceptually, the process looks like this:

```text
x ───► 10

↓

create object 15

↓

x ───► 15
```

The original object is never modified.

That's why `id()` changes.

---

Now let's look at a list.

```python
numbers = [1, 2]
```

Then we execute:

```python
numbers += [3]
```

Many people expect this to behave just like the previous example.

But lists are mutable objects.

That means Python can modify the existing object instead of creating a new one.

Conceptually, it's very similar to writing:

```python
numbers.append(3)
```

Or, when multiple elements are involved:

```python
numbers.extend([3])
```

The list itself remains the same object.

Only its contents change.

That's why `id()` stays the same.

---

Let's compare the two cases side by side.

With numbers:

```python
x = 10

before = id(x)

x += 5

after = id(x)
```

`before` and `after` will be different.

With lists:

```python
numbers = [1, 2]

before = id(numbers)

numbers += [3]

after = id(numbers)
```

This time, `before` and `after` are identical.

---

This reveals an important principle.

The `+=` operator doesn't, by itself, determine whether a new object will be created.

Instead, it asks the object to perform an in-place addition **if possible**.

What happens next depends entirely on the object itself.

If the object can be modified, Python modifies it.

If it can't, Python creates a new object instead.

That's why the exact same operator behaves differently in different situations.

---

There's one more interesting example.

Consider this code:

```python
numbers = [1, 2]
other = numbers

numbers += [3]

print(other)
```

What do you think it prints?

If you've been following the previous articles, you already know the answer:

```python
[1, 2, 3]
```

Why?

Because `+=` modified the existing list.

Both names continued to refer to the same object.

Now compare that with numbers:

```python
x = 10
y = x

x += 5

print(y)
```

The result is:

```python
10
```

This time, a new object was created.

The name `x` now refers to the new object, while `y` continues referring to the original one.

---

We can now summarize the rule.

The `+=` operator does **not** guarantee that an existing object will be modified.

Nor does it guarantee that a new object will be created.

It simply invokes the behavior defined by the object itself.

For mutable objects, that usually means modifying the object in place.

For immutable objects, it means creating a new object instead.

---

If this still feels a little magical, don't worry.

There's no magic involved.

Every Python object defines how it responds to different operations.

That's why the very same operator can produce completely different behavior depending on the object it's working with.

---

This naturally leads to another interesting question.

We already know that objects can be copied.

But what does a "copy" actually mean?

If you copy a list, are nested lists copied too?

And why does modifying a copy sometimes seem to change the original?

That's exactly what we'll explore in the next article.
