---
title: 'Numbers and Strings'
pubDate: 2026-07-03 17:46:37
description: 'In the previous article, we learned how to store data in variables. But what kinds of data can Python actually store?'
tags: ["int", "float", "str", "literals", "python", "variables", "data types"]
---

In the previous article, we learned how to store data in variables.

But what kinds of data can Python actually store?

For example:

```python
age = 25
```

or

```python
name = "Anna"
```

In the first case, we're storing a **number**.

In the second, we're storing **text**.

These are the first two data types every Python programmer learns.

---

## Numbers

If a value is written without quotes, Python treats it as a number.

For example:

```python
age = 25
year = 2026
temperature = -5
```

You can perform ordinary arithmetic with numbers.

```python
print(2 + 3)
print(10 - 4)
print(6 * 7)
print(20 / 5)
```

The output is:

```text
5
6
42
4.0
```

Python can add, subtract, multiply, and divide numbers just like a calculator.

---

## Integers and Floating-Point Numbers

There are two main kinds of numbers in Python.

Integers:

```python
10
0
-15
```

Their type is called `int`.

Floating-point numbers:

```python
3.14
2.5
-0.01
```

Their type is called `float`.

For now, it's enough to remember:

- `int` - whole numbers;
- `float` - numbers with a fractional part.

---

## Strings

Any text in Python is written inside quotation marks.

For example:

```python
name = "Anna"
city = "London"
message = "Hello!"
```

These values are called **strings**.

Their type is `str`.

It doesn't matter whether a string contains a single character or an entire paragraph.

It's still a string.

---

## Why Do We Need Quotes?

Compare these two examples.

```python
print(100)
```

and

```python
print("100")
```

They produce the same output:

```text
100
```

But to Python, they're completely different kinds of data.

The first is a number.

The second is a string.

The quotation marks are what tell Python the difference.

---

## Numbers and Strings Behave Differently

For example:

```python
print(2 + 3)
```

produces:

```text
5
```

But if we write:

```python
print("2" + "3")
```

the result is:

```text
23
```

Why?

Because Python doesn't add strings the way it adds numbers.

Instead, it joins them together into a single string.

---

## What Is a Literal?

When we write:

```python
age = 25
```

the value `25` appears directly in our source code.

This is called a **literal**.

The same is true for strings.

```python
name = "Anna"
```

The string `"Anna"` is also a literal.

For now, just remember this simple definition:

> A literal is a value written directly in your program.

---

## What We Learned Today

Today we met Python's first data types.

- `int` represents integers.
- `float` represents floating-point numbers.
- `str` represents strings.
- Text is always written inside quotation marks.
- Numbers and strings may look similar, but Python treats them differently.
- A value written directly in your code is called a **literal**.

---

## Try It Yourself

Create a new Python file and run this code.

```python
age = 25
height = 1.82
name = "Anton"

print(age)
print(height)
print(name)

print(10 + 5)
print("10" + "5")
```

Then experiment with it.

For example:

- replace the name with your own;
- try your favorite number;
- modify the strings and see what changes.

The best way to learn is to play with the code yourself.

---

## What's Next?

So far, every value has been written directly into the program.

But most programs get their data from the user.

In the next article, we'll learn how to read input from the keyboard using `input()` and display results on the screen with `print()`.
