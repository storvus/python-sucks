---
title: 'Mutable and Immutable Objects in Python'
pubDate: 2026-06-20 14:35:26
description: 'Python divides all objects into two large groups. The first group is called mutable objects. The second is immutable objects.'
tags: ["python", "types", "immutable", "mutable"]
---
In the previous article, we discovered something interesting.

Lists can be modified:
```python
numbers = [1, 2]

numbers.append(3)

print(numbers)
```

The output is:
```python
[1, 2, 3]
```
Numbers, however, behave differently.

When we write:
```python
x = 10
x = 20
```
the object `10` doesn't somehow become `20`. Instead, the name `x` simply becomes bound to a different object.

At first glance, these seem like two completely different behaviors.

In reality, they come from one of Python's most fundamental ideas.

Python divides its objects into two broad categories:

* mutable objects
* immutable objects

---

Let's start with mutable objects.

A mutable object is one whose internal state can be changed after it's created.

Lists are the classic example.

Suppose we create a list:
```python
numbers = [1, 2]
```
We can then add elements:
```python
numbers.append(3)
```
remove them:
```python
numbers.remove(2)
```
or replace existing values:
```python
numbers[0] = 100
```
In every case, Python is working with the same object.

The object isn't replaced or recreated.

Only its contents change.

That's why multiple names referring to the same list all observe the same changes.

---

Now let's look at immutable objects.

Once an immutable object has been created, its state can never change.

Take a number:
```python
x = 10
```
Now assign a different value:
```python
x = 20
```
It may look as though the object changed.

But that's not what happened.

The object `10` remains exactly as it was.

The name `x` simply stops referring to it and becomes bound to another object instead.

The same idea applies to strings.

Suppose we write:
```python
name = "Python"
```
Now we "add" some text:
```python
name = name + " 3"
```
It looks like the string has been modified.

In reality, Python creates an entirely new string:
```python
"Python 3"
```
and rebinds the name `name` to it.

The original string `"Python"` never changes.

---

At this point, it's worth emphasizing one important idea.

When we describe an object as mutable or immutable, we're talking about the object itself.

Not the variable.

Not the name.

Not the assignment statement.

The property belongs to the object that exists in memory.

This distinction may seem subtle now, but it'll help us avoid many common mistakes later on.

---

So which built-in objects are immutable?

Some of the most common examples are:
```python
10
3.14
True
"hello"
(1, 2, 3)
```
These include:

* integers;
* floating-point numbers;
* booleans;
* strings;
* tuples.

Once created, none of these objects can be modified.

Common mutable objects include:
```python
[1, 2, 3]
{"name": "Anton"}
{"python", "java"}
```
These are:

* lists;
* dictionaries;
* sets.

Their contents can be changed after they're created.

---

At this point, you might be wondering:

If mutable objects are so flexible, why isn't everything mutable?

The answer is that immutable objects offer several important advantages.

Since they can never change, Python can safely share and reuse them in many situations, compare them efficiently, and make certain internal optimizations.

They're also easier to reason about.

If an object is immutable, you never have to worry that some other part of your program has modified it behind your back.

That's why Python includes both mutable and immutable objects.

Each serves a different purpose.

---

We can now summarize Python's object model a little more precisely.

When you write:
```python
x = something
```
Python doesn't store a value inside a variable.

It binds a name to an object.

What happens next depends on the object itself.

If the object is mutable, its state can be modified in place.

If it's immutable, any apparent "change" results in a different object, with the name simply being rebound to it.

---

Now we're finally ready for another interesting question.

Suppose we have two lists containing exactly the same values:
```python
a = [1, 2, 3]
b = [1, 2, 3]
```
Are they actually the same object?

Or are they merely equal?

And why does Python sometimes use `==`, while other times `is` is the right choice?

That's exactly what we'll explore in the next article. 🚀
