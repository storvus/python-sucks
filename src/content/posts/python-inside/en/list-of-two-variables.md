---
title: 'Why Does a List Change in Two Variables?'
pubDate: 2026-06-10 20:58:08
description: "In the previous article, we learned that variables in Python don't store data themselves. Instead, a name simply refers to an object. With numbers, this feels quite intuitive. But as soon as we start working with lists, Python's behavior often surprises people."
tags: ["python", "list",]
---
In the previous article, we learned that variables in Python don't store data themselves. Instead, a name simply refers to an object.

With numbers, this feels quite intuitive:

```python
x = 10
y = x
```
Both names refer to the same object whose value is `10`.

So far, everything seems straightforward.

But as soon as we start working with lists, Python's behavior often surprises people.

Consider this example:
```python
a = [1, 2]
b = a

a.append(3)

print(b)
```
Many beginners expect the output to be:
```python
[1, 2]
```
After all, we modified `a`, not `b`.

Instead, Python prints:
```python
[1, 2, 3]
```
It looks as if changing one variable somehow changed the other.

At first glance, it may seem like Python is keeping the two variables synchronized behind the scenes.

In reality, the explanation is much simpler.

Let's go back to the idea from the previous article.

When we write:
```python
a = [1, 2]
```
Python creates a list object, and the name `a` becomes bound to it.

Visually:
```
a ───► [1, 2]
```
Next comes this line:
```python
b = a
```
This is the crucial part.

Python does **not** create a second list.

No copy is made.

Instead, the name `b` is bound to exactly the same object.

Now the picture looks like this:
```
a ─┐
   ├──► [1, 2]
b ─┘
```
Notice that there's still only one list.

The only thing that changed is that there are now two names referring to it.

That's why the next line:
```python
a.append(3)
```
doesn't create a new list.

It modifies the existing object.

After the call to `append()`, the picture becomes:
```
a ─┐
   ├──► [1, 2, 3]
b ─┘
```
Since both names refer to the same object, the change is visible through both of them.

In other words, Python didn't modify two different lists.

It modified one list that simply has two names.

This behavior is one of the most common sources of confusion for beginners.

For example, you might write a function that modifies a list passed as an argument, only to discover later that the original list outside the function has changed as well.

From Python's point of view, though, there's nothing mysterious happening.

If multiple names refer to the same object, they all see the object's current state.

At this point, you may be wondering something else.

If a list can be modified without creating a new object, why doesn't the same thing happen with numbers?

For example:
```python
x = 10
y = x

x = 20
```
After this code runs, `y` still refers to `10`.

Why can a list be modified in place, while a number cannot?

That's exactly the question we'll answer in the next article.
