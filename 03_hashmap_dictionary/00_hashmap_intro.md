# Hashmaps / Dictionaries

## Prerequisites

Before learning hashmaps, you should know:

- Arrays / lists
- Loops
- Counting values
- Basic Python syntax

If you completed the **arrays_strings** section, you are ready.

---

## What is a Hashmap?

A hashmap stores data in **key → value pairs**.

Example in Python:

```python
person = {
    "name": "Alice",
    "age": 25
}

print(person["name"])   # Alice
```

Key → value relationship.

---

## Why Hashmaps Are Powerful

Hashmaps allow **very fast lookups**.

Instead of scanning a list again and again, we store information and retrieve it quickly.

Example:

Without hashmap:

```
Check every element
Time: O(n)
```

With hashmap:

```
Direct lookup
Time: O(1)
```

---

## Python Dictionary

In Python, hashmaps are called **dictionaries**.

Example:

```python
freq = {}

freq["apple"] = 1
freq["banana"] = 2

print(freq)
```

Output:

```
{'apple': 1, 'banana': 2}
```

---

## Basic Dictionary Operations

### Create

```python
freq = {}
```

---

### Add value

```python
freq["apple"] = 1
```

---

### Update value

```python
freq["apple"] += 1
```

---

### Check if key exists

```python
if "apple" in freq:
```

---

### Get value safely

```python
freq.get("apple", 0)
```

---

## Why We Use Hashmaps in DSA

Hashmaps help solve many problems faster.

Examples:

- Frequency counting
- Two Sum
- Grouping data
- Detecting duplicates
- Tracking seen values

---

## Time Complexity

Average case:

| Operation | Time |
|------|------|
| Insert | O(1) |
| Lookup | O(1) |
| Update | O(1) |

This makes hashmaps extremely useful.

---

## Beginner Tip

Whenever you see problems like:

- "count occurrences"
- "find duplicates"
- "store seen values"
- "find matching pairs"

Think:

**Maybe a hashmap can help.**

---

## What You Will Learn in This Section

Scripts in this folder:

```
frequency_count.py
two_sum.py
group_anagrams.py
first_unique_char.py
```

Each problem will show how hashmaps simplify complex tasks.

Start with **frequency_count.py**.