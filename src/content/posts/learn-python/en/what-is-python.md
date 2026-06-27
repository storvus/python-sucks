---
title: 'What Does It Mean to "Run Python"?'
pubDate: 2026-06-27 18:07:14
description: "When people say, 'I write Python', they're usually referring to two different things at once. The first is the 'Python language' itself. The second is 'the program that can execute that code'."
tags: ["python", "interpreter", "CPython", "REPL", "script.py", "print"]
---
When people say, **"I write Python,"** they're usually referring to two different things at once.

The first is the **Python language** itself - a set of rules that defines how Python code is written.

For example, this is valid Python code:

```python
print("Hello!")
```

The second is **the program that can execute that code**.

Your computer doesn't understand Python by itself. It needs a special program that reads your code line by line and performs the operations you've written.

That program is called the **Python interpreter**.

---

## Which Python Do You Have Installed?

If you open a terminal and run

```bash
python --version
```

or

```bash
python3 --version
```

you'll see something like

```text
Python 3.14.0
```

Many people assume that this *is* Python.

In reality, it's simply the version of the program that executes Python code.

The Python language itself is defined separately in its official language specification. Different programs can implement that specification.

The most widely used implementation is called **CPython**.

In fact, when people say **Python**, they're almost always referring to CPython.

Other implementations exist (such as PyPy and Jython), but there's no need to worry about them just yet.

---

## The First Way to Run Python: The REPL

The easiest way to try Python is without creating any files.

Simply run

```bash
python
```

or

```bash
python3
```

in your terminal.

You'll see a prompt that looks something like this:

```text
>>>
```

This is called the **REPL**.

It stands for:

- **Read** - read the command you type;
- **Eval** - evaluate it;
- **Print** - display the result;
- **Loop** - wait for the next command.

For example, type:

```python
>>> 2 + 2
```

Python responds with:

```text
4
```

Or try:

```python
>>> print("Hello!")
```

You'll get:

```text
Hello!
```

The REPL is a great place to experiment and try things out.

---

## The Second Way: Running a Script

Most Python code is stored in files.

Let's create a file called

```text
hello.py
```

and put this inside:

```python
print("Hello, world!")
```

Now run:

```bash
python hello.py
```

or

```bash
python3 hello.py
```

The output will be:

```text
Hello, world!
```

This is how most Python programs are executed.

---

## What Does `print()` Do?

For now, you can think of `print()` as a command that says:

> "Display something to the user."

For example,

```python
print("I'm learning Python")
```

prints

```text
I'm learning Python
```

And

```python
print(100)
```

prints

```text
100
```

That's all you need to know for now.

Later, we'll take a closer look at functions and learn why `print` is written this way.

---

## Script or Program?

You'll often hear the word **script**.

In practice, it's just a Python file.

For example:

```text
backup.py
```

or

```text
calculator.py
```

There's nothing magical about the term.

Historically, smaller programs came to be called *scripts*, and the name stuck.

---

## What We Learned Today

Today we introduced several important ideas:

- **Python** is a programming language.
- To execute Python code, you need a **Python interpreter**.
- The most common interpreter implementation is **CPython**.
- Python code can be run in two ways:
  - through the **REPL** (the interactive interpreter);
  - from a Python file (such as `hello.py`).
- The `print()` function displays information on the screen.

---

## Try It Yourself

Create a file called `hello.py` and experiment with it.

For example:

```python
print("Hello!")
print("My name is Anna")
print(123)
print(2 + 3)
```

Try changing the text, the numbers, and the expressions.

See how the output changes.

Don't be afraid to make mistakes - that's one of the best ways to learn a new programming language.

---

## What's Next?

Now that we know how to run Python programs, a new question naturally comes up.

Suppose we write:

```python
name = "John"
```

**Where does Python store that value?**

And what does the `=` operator actually mean?

That's exactly what we'll explore in the next article: **"Variables and Names."**
