---
title: 'Identity and Equality in Python'
pubDate: 2026-06-22 15:41:15
description: "If you ask a beginner what the difference is between is and ==, you'll often hear something like `==` compares values, while `is` compares references."
tags: ["python", "types", "is", "equal", "comparison"]
---
If you ask a beginner what the difference is between `is` and `==`, you'll often hear something like this:

> "`==` compares values, while `is` compares references."

It's a common explanation.

And while it points in the right direction, it isn't quite accurate.

Let's see what's really happening.

We'll start with a simple example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

The output is:

```
True
False
```

At first glance, that seems odd.

If the lists are identical, why does one comparison return `True` while the other returns `False`?

To answer that, let's recall what we've learned in the previous articles.

In Python, variables don't contain objects.

Names refer to objects.

When we execute:

```python
a = [1, 2, 3]
```

Python creates a list object.

Then we execute:

```python
b = [1, 2, 3]
```

This creates **another** list object.

Even though both lists contain exactly the same values, they are two distinct objects.

Visually:

```
a ───► [1, 2, 3]

b ───► [1, 2, 3]
```

Now the behavior of the two operators becomes much easier to understand.

The `==` operator asks:

> Do these objects have the same value?

In this case, they do.

So:

```python
a == b
```

returns:

```
True
```

The `is` operator asks a completely different question:

> Are these the very same object?

This time, the answer is no.

So:

```python
a is b
```

returns:

```
False
```

In other words:

- `==` compares an object's value
- `is` compares an object's identity

Now consider a different example:

```python
a = [1, 2, 3]
b = a

print(a == b)
print(a is b)
```

This time, both comparisons return:

```
True
True
```

Why?

Because no second list was ever created.

The assignment:

```python
b = a
```

simply gives the existing object another name.

Now the picture looks like this:

```
a ─┐
   ├──► [1, 2, 3]
b ─┘
```

Since both names refer to the same object:

- the values are equal
- and the identity is the same

That's why both operators return `True`.

---

At this point, you might wonder:

If `is` only checks whether two names refer to the same object, why do we need it at all?

Why not always use `==`?

Most of the time, `==` is exactly what you want.

Use it whenever you're comparing values - for example, numbers, strings, or lists.

But sometimes the identity of an object matters more than its value.

The best-known example is `None`.

You've probably seen code like this:

```python
if value is None:
    ...
```

Notice that it uses `is`, not `==`. Why?

Because there's only one `None` object in a Python program.

We're not asking whether another object happens to behave like `None`.

We're asking whether this is the `None` object.

That's why the Python community recommends writing:

```python
if value is None:
```

instead of:

```python
if value == None:
```

It clearly communicates your intent and is considered the idiomatic way to write the comparison.

---

You may occasionally run into something even more surprising:

```python
a = 10
b = 10

print(a is b)
```

On many Python implementations, this prints:

```
True
```

But based on everything we've discussed so far, you might have expected `False`.

Don't worry - this doesn't mean numbers behave differently.

Python sometimes reuses certain small immutable objects as an internal optimization.

Small integers are one example.

The important thing is that your code should never rely on this behavior.

If you're comparing values, use `==`.

If you're checking whether two names refer to the same object, use `is`.

---

We can now summarize the difference with one simple rule.

If you're asking:

> "Do these objects have the same value?"

use `==`.

If you're asking:

> "Are these the same object?"

use `is`.

That's exactly why the previous articles in this series were so important.

Without understanding objects and names, the difference between `is` and `==` feels like an arbitrary rule you have to memorize.

Once you understand Python's object model, though, the distinction becomes completely natural.
