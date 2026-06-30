---
title: 'Variables and Names'
pubDate: 2026-06-30 18:27:43
description: "Now it's time to understand how Python stores data."
tags: ["variable", "assignment", "name", "identifier"]
---
In the previous article, we learned how to run Python programs.

Now it's time to understand how Python stores data.

Consider this line of code:

```python
name = "Anna"
```

Most programming languages would describe `name` as a **variable**.

Python programmers use that term too.

However, there's a more precise way to think about it:

`name` is a **name**.

---

## What Does `=` Actually Do?

This statement:

```python
name = "Anna"
```

means:

> Create the name `name` and bind it to the value `"Anna"`.

After that, we can use the name anywhere in our program.

```python
print(name)
```

The output is:

```text
Anna
```

---

## A Name Can Be Used Many Times

For example:

```python
name = "Anna"

print(name)
print(name)
print(name)
```

The result is:

```text
Anna
Anna
Anna
```

Each time, Python looks up the value currently associated with the name `name`.

---

## A Name Can Be Rebound

Later, we can write:

```python
name = "John"
```

Now:

```python
print(name)
```

prints:

```text
John
```

The name now refers to a different value.

---

## Naming Rules

A name may contain letters, digits, and underscores.

For example:

```python
user
user_name
age
counter2
```

There are a few simple rules.

A name **cannot** begin with a digit.

This is invalid:

```python
2users = 10
```

Names also cannot contain spaces.

This is incorrect:

```python
user name = "Anna"
```

Instead, write:

```python
user_name = "Anna"
```

---

## Choosing Good Names

A good name should describe what it represents.

For example:

```python
age = 18
```

is much more informative than:

```python
x = 18
```

Code that's easy to read is usually easier to understand and maintain.

For example:

```python
user_name = "Anna"
print(user_name)
```

Even someone seeing the project for the first time can immediately understand what the code is doing.

---

## Reserved Words

Some words already have special meaning in Python.

For example:

```python
if
for
while
class
```

These are **keywords**, and they can't be used as names.

For example:

```python
for = 10
```

results in a syntax error.

---

## What We Learned Today

Today we introduced one of the most fundamental concepts in Python.

- A **name** allows us to refer to data.
- The `=` operator binds a name to a value.
- The same name can be used many times.
- Later, a name can be rebound to a different value.
- Good names make code easier to read.
- Python keywords cannot be used as names.

---

## Try It Yourself

Create a new Python file and experiment with it.

```python
name = "Anna"
age = 20

print(name)
print(age)

name = "John"

print(name)
```

Try changing the values and the names.

For example, replace `"Anna"` with your own name, or add another variable called `city`.

---

## What's Next?

Now we know how to associate names with values.

But what kinds of values can Python store?

Why does this work:

```python
age = 18
```

just as well as this?

```python
name = "Anna"
```

In the next article, we'll meet Python's two most fundamental data types:

**numbers** and **strings**.
