---
title: 'What Does the `del` Statement Actually Do?'
pubDate: 2026-07-12 21:52:18
description: "To answer that question, let's revisit one of the very first ideas we learned in this series."
tags: ["python", "del", "variables", "delete"]
---

> This article assumes you're already comfortable writing simple Python programs and know the basics (`if`, `for`, functions, and lists). Here we're not learning **how** to use Python—we're learning **why** it behaves the way it does.

Try to guess what this code prints.

```python
numbers = [1, 2, 3]
other = numbers

del numbers

print(other)
```

Many people expect this program to fail.

After all, we just deleted the list.

But Python happily prints:

```python
[1, 2, 3]
```

That seems odd.

We deleted the list...

So why does it still exist?

---

To answer that question, let's revisit one of the first ideas from this series.

When we write:

```python
numbers = [1, 2, 3]
```

the variable doesn't store the list itself.

Python creates a list object.

Then the name `numbers` is bound to that object.

Later, we execute another line:

```python
other = numbers
```

Now two names refer to the same object.

Visually:

```text
numbers  ─┐
          │
          ▼
      [1, 2, 3]
          ▲
          │
other ────┘
```

Now comes the interesting part.

```python
del numbers
```

What actually happens?

Many people imagine that Python destroys the object.

But that's not what `del` does.

In fact, `del` doesn't operate on objects at all.

It operates on **names**.

After this statement, the picture looks like this:

```text
      [1, 2, 3]
          ▲
          │
other ────┘
```

The name `numbers` is gone.

The object is not.

It still exists because the name `other` continues to refer to it.

That's why the next line:

```python
print(other)
```

prints the list without any problem.

---

Now let's try a different example.

```python
numbers = [1, 2, 3]

del numbers

print(numbers)
```

This time, the program really does fail.

But it's important to understand why.

The error doesn't occur because Python can't find the object.

It occurs because the name `numbers` no longer exists.

When Python executes:

```python
print(numbers)
```

it tries to look up the name `numbers`.

But there is no such name anymore.

So Python raises:

```python
NameError
```

Notice what the exception is telling us.

It's complaining about the **name**.

Not about the object.

---

You can think of `del` as breaking the connection between a name and an object.

Whether the object itself continues to exist is a separate question.

And the answer depends on just one thing.

Is there still at least one name referring to that object?

---

Let's look at one more example.

```python
numbers = [1, 2, 3]

other = numbers

third = numbers

del numbers
del other

print(third)
```

What happens now?

By this point, the answer should be obvious.

The list continues to exist.

Why?

Because the name `third` still refers to it.

You can delete ten different names if you like.

As long as at least one name still points to the object, the object remains alive.

---

This leads to an interesting question.

What happens when the **last** name disappears?

For example:

```python
numbers = [1, 2, 3]

del numbers
```

Now nothing in our program appears to refer to the object anymore.

Does Python immediately remove it from memory?

Or are there other rules involved?

That's exactly what we'll explore in the next article.
