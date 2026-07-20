---
title: 'When Is an Object Actually Deleted?'
pubDate: 2026-07-20 20:51:34
description: 'If an object continues to exist after its name is deleted, who decides when it can finally be removed from memory?'
tags: ["python", "del", "variables", "delete", "reference counting", "garbage collector"]
---

> This article assumes you're already comfortable writing simple Python programs and know the basics (`if`, `for`, functions, and lists). Here we're not learning **how** to use Python - we're learning **why** it behaves the way it does.

In the previous article, we learned that the `del` statement doesn't delete an object.

It only deletes a name.

That naturally raises another question.

If an object can continue to exist after its name has been deleted, who decides when it can finally be removed from memory?

Let's find out.

Imagine the simplest possible example.

```python
numbers = [1, 2, 3]
```

After this line executes, there is one list object.

One name refers to it.

Visually:

```text
numbers ───► [1, 2, 3]
```

Now we introduce another name.

```python
other = numbers
```

The picture becomes:

```text
numbers  ─┐
          │
          ▼
      [1, 2, 3]
          ▲
          │
other ────┘
```

Two names.

One object.

---

Now let's execute:

```python
del numbers
```

What happens?

We already know the answer.

The name disappears.

The object doesn't.

```text
      [1, 2, 3]
          ▲
          │
other ────┘
```

This gives us a very simple rule.

As long as at least one reference to an object still exists, the object stays alive.

---

Now let's delete the second name as well.

```python
del other
```

The picture now looks very different.

```text
[1, 2, 3]
```

Nothing refers to the object anymore.

There's no way to access it by name.

There's no way to modify it.

There's no way to use it.

From the program's point of view, the object has become completely unreachable.

That's the moment Python realizes that nothing can ever use this object again.

---

You can imagine every object constantly asking itself a very simple question:

> **"Can anything still reach me?"**

If the answer is **yes**, the object stays alive.

If the answer is **no**, its memory can eventually be reclaimed.

---

At first, it might seem that Python would have to search through the entire program every time to see whether any references are still pointing to an object.

Fortunately, it doesn't.

Python uses a much simpler idea.

Imagine that every object has a small counter attached to it.

Whenever a new reference to the object is created, the counter increases.

For example:

```python
numbers = [1, 2, 3]
```

The counter is now:

```text
[1, 2, 3]
references: 1
```

After:

```python
other = numbers
```

it becomes:

```text
[1, 2, 3]
references: 2
```

After:

```python
third = numbers
```

it becomes:

```text
[1, 2, 3]
references: 3
```

If we then execute:

```python
del other
```

the counter decreases:

```text
[1, 2, 3]
references: 2
```

After deleting another name:

```python
del numbers
```

it becomes:

```text
[1, 2, 3]
references: 1
```

Only when the final reference disappears does the counter reach zero.

```text
[1, 2, 3]
references: 0
```

At that point, Python knows:

> "Nothing can access this object anymore."

Its memory can now be reclaimed.

---

This memory management technique is called **reference counting**.

It's one of the fundamental ideas behind **CPython**, the most widely used implementation of Python.

Don't worry if the term sounds unfamiliar.

We've actually been using this mental model throughout the last several articles.

Now it finally has a name.

---

At this point, you might wonder:

Does that mean the problem is completely solved?

If Python keeps track of references, why does it need any additional memory management at all?

Unfortunately, there's one situation that simple reference counting can't handle.

Imagine two objects that refer to each other.

```python
a = []
b = []

a.append(b)
b.append(a)
```

Now delete both names:

```python
del a
del b
```

The two objects still refer to each other.

They form a cycle.

Nothing in the program can reach them anymore.

Yet neither object's reference count ever drops to zero.

Does that mean this memory stays allocated forever?

Fortunately, no.

To deal with situations like this, Python uses another mechanism called the **Garbage Collector (GC)**.

We'll see how it works - and why Python needs it - in the next article.
