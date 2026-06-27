---
title: 'Why Numbers Behave Differently from Lists'
pubDate: 2026-06-17 17:17:17
description: "It almost looks as if Python somehow 'links' variables together. But that's not what's happening."
tags: ["python", "types", "immutable", "mutable"]
---
> We assume you already know how to write simple Python programs and understand basic syntax (if, for, functions, lists). Here, we're not discussing how to use the language, but why it works the way it does. 

The previous article, we saw something that can seem quite surprising at first:
```python
a = [1, 2]
b = a

a.append(3)

print(b)  # [1, 2, 3]
```

It almost looks as if Python somehow "links" variables together.

But that's not what's happening.

The variables aren't connected to each other - they simply refer to the same object.

That naturally leads to another question.

If a list can be modified _in place_, why don't numbers behave the same way?

Consider this example:
```python
x = 10
y = x

x = 20

print(y)
```
This time, the output is:
```python
10
```
`y` still refers to `10`, even though we reassigned `x`.

Why?

The answer lies in one subtle but fundamental idea.

Not all Python objects behave the same way when you try to "change" them.

Let's start with numbers.

When we write:
```python
x = 10
```
Python creates the object `10`, and the name `x` becomes bound to it:
```
x ───► 10
```
Now we execute:
```python
x = 20
```
This is where it's important to separate **rebinding a name** from **modifying an object**.

The object `10` does **not** turn into `20`.

In fact, the object `10` doesn't change at all.

Instead, Python creates (or reuses) the object `20`, and the name `x` is simply rebound to it.

Now the picture looks like this:
```
x ───► 20

y ───► 10
```
The object `10` still exists because `y` continues to refer to it.

Now let's compare that to a list.
```python
a = [1, 2]
```
This creates a single list object:
```
a ───► [1, 2]
```
Now comes the important part:
```python
a.append(3)
```
Unlike assignment, `append()` does **not** create a new list.

Instead, it modifies the existing object in place.

After the call, we have:
```
a ───► [1, 2, 3]
```
If we originally had two names:
```python
a = [1, 2]
b = a
```
the picture looked like this:
```
a ─┐
   ├──► [1, 2]
b ─┘
```
Calling:
```python
a.append(3)
```
doesn't change the names.

It changes the object itself.

As a result, both names still refer to the same list-but that list now has different contents:
```
a ─┐
   ├──► [1, 2, 3]
b ─┘
```
This brings us to the key difference.

The number `10` cannot be modified.

A list can.

This isn't a special rule for numbers or lists, and it isn't a quirk of Python's syntax.

It's a fundamental property of Python objects.

Some objects can never change after they're created.

Whenever they appear to "change," Python actually creates a different object and rebinds the name.

Other objects allow their internal state to be modified without creating a new object.

That's why:

* numbers behave as **unchangeable** objects;
* lists behave as **changeable** objects.

Here's a useful way to think about it.

An unchangeable object is frozen once it's created.

If you need a different value, you need a different object.

A changeable object, on the other hand, remains the same object even though its contents can change.

Now the difference between numbers and lists becomes much easier to understand.

With numbers, changing the value always means referring to a different object.

With lists, you're usually modifying the existing object instead.

This leads to an important principle that we'll keep coming back to throughout this series:

> In Python, a program's behavior is determined not by what's "stored in a variable," but by whether you're modifying an object or simply rebinding a name.

Now we can finally introduce the official terminology.

The kinds of objects we've been talking about are called:

* **mutable objects**
* **immutable objects**

By now, though, these shouldn't feel like abstract definitions.

They're simply names for the behaviors we've already observed.

In the next article, we'll take a closer look at mutable and immutable objects, see which built-in types belong to each category, and understand why this distinction is so fundamental to Python itself.
