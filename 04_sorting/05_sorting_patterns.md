# Sorting Patterns

Sorting is one of the most useful techniques in problem solving.

Many difficult problems become much easier if we **sort the data first**.

Typical flow:

```
Sort → Scan → Solve
```

Sorting often reduces complex problems into **simple comparisons between neighbors**.

---

# Pattern 1 — Sort + Scan

After sorting, related elements usually appear **next to each other**.

This makes it easy to detect patterns.

Example:

```
[4, 2, 7, 2, 9]
```

After sorting:

```
[2, 2, 4, 7, 9]
```

Now duplicates are easy to detect because they are **adjacent**.

### Example problems

* Detect duplicates
* Remove duplicates
* Find closest numbers

### Example idea

```python
nums.sort()

for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        print("Duplicate found")
```

---

# Pattern 2 — Sort + Merge

When dealing with **intervals**, sorting helps bring overlapping intervals together.

Example:

```
Intervals:
[5,7] [1,3] [2,6]
```

After sorting:

```
[1,3] [2,6] [5,7]
```

Now overlapping intervals appear next to each other and can be merged.

### Example problems

* Merge intervals
* Meeting room scheduling
* Calendar conflicts

### Idea

```
Sort intervals by start
Scan and merge overlaps
```

### File in this repo

```
merge_intervals.py
```

---

# Pattern 3 — Sort + Two Pointers

Sorting often allows us to use the **two pointer technique**.

Example:

Find two numbers that sum to a target.

```
nums = [8, 1, 4, 6]
target = 10
```

After sorting:

```
[1, 4, 6, 8]
```

Now we can use:

```
left pointer
right pointer
```

### Idea

```
left + right
if too small → move left
if too large → move right
```

This avoids checking every pair.

### Example problems

* Two sum in sorted array
* Closest pair
* Container problems

---

# Pattern 4 — Sort + Custom Key

Sometimes we need to sort using a **specific rule**.

Examples:

* sort words by length
* sort intervals by end time
* sort students by score

Python allows custom sorting using:

```
key=
```

### Example

```python
words = ["apple", "fig", "banana"]

sorted(words, key=len)
```

Result:

```
['fig', 'apple', 'banana']
```

### File in this repo

```
custom_sort.py
```

---

# Pattern 5 — Sort + Greedy

Many greedy algorithms start with sorting.

Example:

Scheduling problems.

Intervals sorted by **earliest finishing time** often lead to optimal solutions.

Example:

```
Sort tasks by finish time
Pick the earliest finishing task
Repeat
```

### Example problems

* Interval scheduling
* Minimum meeting rooms
* Activity selection

---

# When Should You Think About Sorting?

Sorting is often useful when a problem mentions:

* intervals
* duplicates
* closest values
* scheduling
* merging ranges
* comparing neighbors
* selecting smallest / largest repeatedly

Ask yourself:

```
Would sorting simplify the problem?
```

---

# Time Complexity Reminder

Sorting usually costs:

```
O(n log n)
```

But it often replaces slower approaches like:

```
O(n²)
```

So overall performance may improve.

---

# Key Takeaway

Sorting is not just about ordering numbers.

It is a **problem solving strategy**.

Many algorithms follow this structure:

```
1. Sort the data
2. Scan the list
3. Apply a simple rule
```

Learning to recognize when sorting helps is a **major step toward solving algorithm problems efficiently**.
