# Hashmap / Dictionary Patterns

This section introduced one of the most important tools in problem solving: **hashmaps (Python dictionaries).**

A hashmap allows us to **store and look up information very quickly**.

Typical operations are **O(1)** on average:

* insert
* lookup
* update

This makes hashmaps extremely useful in many coding interview problems.

---

# Pattern 1 — Frequency Counting

**Idea:**
Count how many times something appears.

Instead of repeatedly scanning the list or string, store the counts in a dictionary.

### Example problems

* Counting characters
* Finding duplicates
* Finding unique elements
* Most frequent element

### Example

```python
counts = {}

for ch in s:
    counts[ch] = counts.get(ch, 0) + 1
```

### Files in this repo

```
frequency_count.py
first_unique_char.py
```

---

# Pattern 2 — Seen Before (Fast Lookup)

**Idea:**
Store elements as you see them so you can quickly check if something already appeared.

Instead of using nested loops, use a hashmap for instant lookup.

### Example problems

* Detect duplicates
* Check if element exists
* Find repeated numbers

### Example

```python
seen = set()

for num in nums:
    if num in seen:
        print("Duplicate found")
    seen.add(num)
```

### Why it helps

Without hashmap:

```
O(n²)
```

With hashmap:

```
O(n)
```

---

# Pattern 3 — Complement Lookup

This pattern appears in **pair problems**.

Instead of checking every pair, calculate the **value you need**.

### Example problem

**Two Sum**

If:

```
num + needed = target
```

Then:

```
needed = target - num
```

Check if the needed value already exists in the hashmap.

### Example

```python
seen = {}

for i, num in enumerate(nums):
    needed = target - num
    
    if needed in seen:
        return [seen[needed], i]
        
    seen[num] = i
```

### Files in this repo

```
two_sum.py
```

---

# Pattern 4 — Grouping Using Keys

Sometimes different inputs should belong to the **same group**.

A hashmap can collect them together.

### Example problem

**Group Anagrams**

Words that share the same letters should be grouped.

We create a **key** that represents the word.

Example:

```
eat -> aet
tea -> aet
ate -> aet
```

All three share the same key.

### Example

```python
groups = {}

for word in words:
    key = "".join(sorted(word))
    
    if key not in groups:
        groups[key] = []
        
    groups[key].append(word)
```

### Files in this repo

```
group_anagrams.py
```

---

# Pattern 5 — Two Pass Problems

Sometimes we must **collect information first**, then **use it later**.

### Example

1️⃣ Count characters
2️⃣ Find first unique

```python
# pass 1
counts = {}

for ch in s:
    counts[ch] = counts.get(ch, 0) + 1

# pass 2
for i, ch in enumerate(s):
    if counts[ch] == 1:
        return i
```

### Files in this repo

```
first_unique_char.py
```

---

# When Should You Think About Hashmaps?

If a problem mentions:

* frequency
* duplicate
* unique
* pair
* grouping
* fast lookup
* counting

A **hashmap is often the right tool.**

---

# Quick Pattern Cheat Sheet

| Pattern            | Idea                   | Example Problem        |
| ------------------ | ---------------------- | ---------------------- |
| Frequency Counting | Count occurrences      | First Unique Character |
| Seen Before        | Store visited elements | Detect duplicates      |
| Complement Lookup  | Find matching value    | Two Sum                |
| Grouping           | Collect similar items  | Group Anagrams         |
| Two Pass           | Gather then use info   | First Unique Character |

---

# Key Takeaway

Most beginners try to solve these problems with **nested loops**.

That leads to:

```
O(n²)
```

A hashmap often reduces this to:

```
O(n)
```

Learning to recognize these patterns is a **big step toward solving problems faster and more confidently.**
