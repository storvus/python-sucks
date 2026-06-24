---
title: 'What Really Happens When You Write x = 10'
pubDate: 2026-06-03 20:03:01
description: 'At first glance it sounds obvious. We imagine a variable as a box in memory where you put a value. But Python works a little differently - and understanding that difference explains a lot.'
tags: ["python", "objects", "types"]
---

If you ask a beginner what this line of code does:
```python
x = 10
```

the answer is usually something like:

> "The number 10 is stored in the variable x."

At first glance, that sounds perfectly reasonable. We're used to thinking of a variable as a box or a memory cell that can hold a value. First the box is empty, then we put a number, a string, or a list into it.

The problem is that Python doesn't actually work that way.

To understand many of Python's behaviors, it's helpful to stop thinking of variables as containers for data. Instead, think of a variable as a **name** that refers to an **object**.

When Python executes:
```python
x = 10
```
it doesn't start with the variable - it starts with the object `10`.

The number `10` is an object. Once that object exists, the name `x` is bound to it.

Visually, you can think of it like this:
```
x ───► 10
```
The arrow indicates that the name `x` refers to the object whose value is `10`.

At first, this distinction may seem unimportant. What difference does it make whether the number is stored inside the variable or the variable simply points to it?

As it turns out, the difference is enormous, and it explains many of Python's most important behaviors.

Now suppose we add another line:
```python
y = x
```
Many people expect Python to create a second copy of the number and store it in another variable.

That's not what happens.

Instead, the name `y` is simply bound to the very same object that `x` already refers to.

Now the picture looks like this:
```
x ─┐
   ├──► 10
y ─┘
```
There's still only one object, but now there are two names that refer to it.

That's why Python makes a clear distinction between **objects** and **names**.

Objects hold data.

Names allow you to access those objects.

Things become even more interesting when a variable appears to "change."

Consider this code:
```python
x = 10
x = 20
```
If you think of variables as boxes, it's natural to imagine that the number `10` inside the box has somehow been replaced with `20`.

But that's not what Python does.

Initially, the name `x` refers to the object `10`:
```python
x ───► 10
```
After the second assignment, the name refers to a different object:
```python
x ───► 20
```
The object `10` hasn't changed, disappeared, or turned into `20`.

The name `x` has simply been rebound to another object.

This may seem like a subtle detail, but it's one of the fundamental ideas behind Python's execution model.

Later, we'll see that it explains many things that often confuse beginners:

* why modifying a list can unexpectedly affect another variable;
* why `is` and `==` are not the same;
* why strings behave differently from lists;
* and how Python passes arguments to functions.

For now, remember just one idea.

When you write:
```python
x = 10
```

Python doesn't put the number into a variable.

It binds the name `x` to the object `10`.

That's why experienced Python developers usually don't say that _a variable stores a value_. Instead, they say that _a name refers to an object_.

It may sound a little less intuitive at first, but it's much closer to how Python actually works.
