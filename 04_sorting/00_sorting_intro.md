# Sorting Introduction

Sorting is one of the most common operations in programming.

Sorting means **arranging data in a specific order**.

Most of the time we sort in:

* ascending order (small → large)
* descending order (large → small)

Example:

Before sorting

```
[5, 2, 8, 1, 3]
```

After sorting

```
[1, 2, 3, 5, 8]
```

---

# Why Sorting Is Important

Many problems become **much easier after sorting**.

Sorting helps because it:

* organizes data
* brings similar values together
* makes searching easier
* allows faster algorithms

For example, instead of checking **every pair**, sorting can help us scan the list in a single pass.

---

# Example: Finding Duplicates

Given:

```
[3, 1, 4, 1, 5]
```

If we sort it:

```
[1, 1, 3, 4, 5]
```

Now duplicates are **next to each other**, which makes them easy to detect.

---

# Example: Interval Problems

Intervals:

```
[5,7]  [1,3]  [2,4]
```

After sorting by starting value:

```
[1,3]  [2,4]  [5,7]
```

Now we can easily detect overlaps and merge intervals.

Sorting often makes these problems much simpler.

---

# Sorting in Python

Python already provides powerful built-in sorting.

Two common ways:

### 1. `sorted()`

Returns a **new sorted list**.

```python
nums = [5, 2, 8, 1]

new_list = sorted(nums)

print(new_list)   # [1,2,5,8]
print(nums)       # original list unchanged
```

---

### 2. `list.sort()`

Sorts the list **in place**.

```python
nums = [5, 2, 8, 1]

nums.sort()

print(nums)   # [1,2,5,8]
```

---

# Sorting Order

Ascending (default):

```python
sorted(nums)
```

Descending:

```python
sorted(nums, reverse=True)
```

---

# Time Complexity

Most efficient sorting algorithms run in:

```
O(n log n)
```

Python’s built-in sort is very efficient and should usually be preferred.

In this section we focus on:

* when sorting helps
* how to use sorting
* problems that become easier after sorting

---

# When Should You Think About Sorting?

Sorting is often useful when a problem involves:

* finding duplicates
* comparing neighbors
* merging intervals
* closest numbers
* grouping similar values
* two pointer techniques

When you see these patterns, consider:

```
Should I sort the data first?
```

Sorting is often the **first step toward a simpler solution**.

---

# What We Will Learn Next

In this section we will cover:

```
basic_sorting.py      → simple sorting algorithms
sort_strings.py       → sorting strings
merge_intervals.py    → interval sorting problems
custom_sort.py        → sorting with custom rules
sorting_patterns.md   → common sorting patterns
```

By the end of this section you will understand **when sorting turns a hard problem into an easy one**.
