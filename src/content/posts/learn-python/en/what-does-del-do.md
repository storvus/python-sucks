---
title: 'Reading Input and Displaying Output'
pubDate: 2026-07-12 21:59:39
description: "So far, every program we've written has behaved exactly the same way. But real programs need to interact with their users."
tags: ["python", "input", "print", "conversion"]
---

So far, every program we've written has behaved exactly the same way.

For example:

```python
print("Hello!")
```

or

```python
age = 25
print(age)
```

Every time we run these programs, they produce exactly the same output.

But most programs need to interact with the user.

In Python, that's what the `input()` function is for.

---

## Reading Input from the User

The simplest example looks like this:

```python
name = input("What's your name? ")
```

When the program reaches this line, it pauses and waits for the user to type something.

For example:

```text
What's your name? Anna
```

After the user presses **Enter**, the text they typed is stored in the variable `name`.

We can then use it later in the program.

```python
print(name)
```

The output is:

```text
Anna
```

---

## Responding to the User

For example:

```python
name = input("What's your name? ")

print("Hello,", name)
```

If the user enters:

```text
Anton
```

the program prints:

```text
Hello, Anton
```

Now the same program can produce different results depending on what the user types.

---

## `input()` Always Returns a String

Let's write another program.

```python
age = input("How old are you? ")

print(age)
```

If the user enters:

```text
25
```

the output is:

```text
25
```

So far, everything looks fine.

But there's an important detail.

To Python, this is **not** a number.

It's a **string**.

---

## Why Does That Matter?

Consider this example.

```python
age = input("Age: ")

print(age + 1)
```

At first glance, it seems like the program should print the user's age plus one.

Instead, it raises an error.

Why?

Because Python doesn't allow you to add a string and a number together.

---

## Converting a String to a Number

To convert text into an integer, we use the `int()` function.

```python
age = int(input("Age: "))
```

Now the program works like this:

1. It reads text from the user.
2. It converts that text into an integer.
3. It stores the result in the variable.

Now we can safely write:

```python
print(age + 1)
```

If the user enters:

```text
25
```

the output is:

```text
26
```

---

## What If the User Doesn't Enter a Number?

What happens if the user types:

```text
twenty-five
```

or

```text
hello
```

Python won't be able to convert that text into an integer.

Instead, the program will terminate with an error.

That's perfectly fine for now.

A little later, we'll learn how to handle situations like this gracefully.

---

## What We Learned Today

Today we made our programs interactive.

- `print()` displays information on the screen.
- `input()` reads input from the user.
- Everything entered through `input()` is initially a string.
- To convert text into an integer, use the `int()` function.

---

## Try It Yourself

Write a program that asks the user for their name and age.

Then print a message like this:

```text
Hello, Anna!
Next year you'll be 26 years old.
```

Here's a hint:

```python
name = input("What's your name? ")
age = int(input("How old are you? "))

print("Hello,", name)
print("Next year you'll be", age + 1, "years old.")
```

Try experimenting.

- Enter different names.
- Change the age.
- Intentionally type text instead of a number and see what happens.

Don't be afraid of errors—they're an important part of learning how programs work.

---

## What's Next?

Our programs can now receive input from the user.

But how can we make them behave differently depending on that input?

For example:

- if the user is older than 18, print one message;
- otherwise, print a different one.

That's exactly what **conditional statements** are for, and we'll explore them in the next article.
