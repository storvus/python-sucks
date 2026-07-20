---
title: 'Conditional Statements'
pubDate: 2026-07-20 21:01:33
description: 'Until now, our programs always executed in the same way. But often a program needs to make decisions.'
tags: ["if", "elif", "else", "bool"]
---

Until now, our programs have always executed in the same way.

For example,

```python
print("Welcome!")
```
will always print the same message, no matter what happens.

But programs often need to make decisions.

For example:

* if a user is an adult - show one message;
* otherwise - show another one.

For this purpose, Python provides the if statement.

---

## The simplest condition

For example,
```python
age = 20

if age >= 18:
    print("Access granted")
```

This code reads almost like a normal sentence:

> If the age is greater than or equal to 18, print the message.

Since the age is 20, the program prints:
```text
Access granted
```

---

## What if the condition is false?

Let's change the age.
```python
age = 15

if age >= 18:
    print("Access granted")
```
Now the program prints nothing.

The condition is `false`, so Python simply skips this block of code.

---

## What does the colon mean?

Pay attention to this line:
```python
if age >= 18:
```
There is a colon after the condition.

It tells Python:

> A block of code that should run only if this condition is true starts here.

---

Why are the lines indented?

Look at the example again:
```python
if age >= 18:
    print("Access granted")
```
The `print()` line starts slightly to the right.

This is called **indentation**.

In Python, indentation has special meaning.

Everything with the same indentation level after an `if` statement belongs to that condition.

For example:
```python
if age >= 18:
    print("Access granted")
    print("Welcome!")
```
Both lines will execute only when the condition is true.

---

## Executing a different action

Very often, we need to do something in the opposite case.

For this, Python provides else.
```python
age = 15

if age >= 18:
    print("Access granted")
else:
    print("Access denied")
```
Now the program always prints one of the two messages.

---

## Multiple options

Sometimes there are more than two possible outcomes.

For example:
```python
score = 85

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
else:
    print("Try again")
```
Python checks conditions from top to bottom.

As soon as one condition is true, the remaining conditions are skipped.

---

## What is a boolean value?

Any condition in Python can be either true or false.

For example:
```python
age >= 18
```
If the age is 20, the result is:

```python
True
```
If the age is 15:

```python
False
```

These values have a special data type called `bool`.

For now, it is enough to remember that every condition eventually becomes either `True` or `False`.

---

## What we learned today

Today we learned how to make programs that can make decisions.

- `if` executes code only when a condition is true.
- `else` provides an alternative option.
- `elif` allows checking additional conditions.
- Indentation defines which lines belong to a condition.
- Every condition in Python evaluates to either `True` or `False`.

---

## Try it yourself

Write a program that asks the user for their age.

If the age is greater than or equal to 18, print:
```text
Welcome!
```
Otherwise, print:
```text
Access denied.
```
After that, try adding another option.

For example:

younger than 14;
between 14 and 17;
18 or older.
What comes next?

Now our program can choose between several options.

But sometimes we need to perform the same action many times.

For example:

- print numbers from 1 to 10;
- ask for a password until it is correct;
- keep running a program until the user gives a command.

For this purpose, Python provides loops.

In the next article, we will learn about the `while` loop.
