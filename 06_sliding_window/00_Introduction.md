# Sliding Window Introduction

The **Sliding Window** technique is a powerful way to process **subarrays or substrings** efficiently.

Instead of repeatedly scanning the same elements, we maintain a **window (range)** that moves across the data.

This technique usually reduces solutions from:

```
O(n²)
```

to:

```
O(n)
```

Sliding Window is closely related to the **two pointer technique**.

---

# Basic Idea

A **window** is a range inside the array.

Example:

```
[1, 2, 3, 4, 5]
```

A window of size 3:

```
[1, 2, 3]
```

Slide it to the right:

```
[2, 3, 4]
```

Slide again:

```
[3, 4, 5]
```

Instead of recalculating everything, we **update the window efficiently**.

---

# Example: Maximum Sum Subarray (Fixed Window)

Problem:

Find the **maximum sum of any subarray of size k**.

Example:

```
nums = [2,1,5,1,3,2]
k = 3
```

Subarrays of size 3:

```
[2,1,5] → sum = 8
[1,5,1] → sum = 7
[5,1,3] → sum = 9
[1,3,2] → sum = 6
```

Maximum sum = **9**

Instead of recalculating each subarray from scratch, we do:

```
remove left value
add next value
```

This makes the algorithm **O(n)**.

---

# Two Types of Sliding Window

## 1. Fixed Window

Window size stays constant.

Example:

```
size = k
```

We move the window one step at a time.

Example problems:

* maximum sum subarray
* average of subarrays
* fixed window statistics

---

## 2. Variable Window

Window size **changes dynamically**.

We expand or shrink depending on conditions.

Example:

```
expand right pointer
shrink left pointer
```

Example problems:

* longest substring without repeating characters
* minimum window substring
* longest subarray with condition

---

# Window Visualization

Example array:

```
[2,1,5,1,3,2]
```

Window size = 3

```
[2,1,5] 1 3 2
 2 [1,5,1] 3 2
 2 1 [5,1,3] 2
 2 1 5 [1,3,2]
```

We move the window across the array.

---

# Sliding Window Structure

Typical algorithm:

```
left = 0

for right in range(len(nums)):

    expand window

    while condition not valid:
        shrink window
        left += 1
```

This structure appears in many problems.

---

# When Should You Think About Sliding Window?

Sliding window is useful when problems involve:

* subarrays
* substrings
* ranges
* contiguous elements
* maximum / minimum over ranges
* longest / shortest sequences

Ask yourself:

```
Can I maintain a window instead of recalculating everything?
```

If yes, sliding window may be the solution.

---

# Time Complexity Advantage

Without sliding window:

```
O(n²)
```

With sliding window:

```
O(n)
```

Because each element is processed only a few times.

---

# What We Will Learn Next

In this section:

```
max_sum_subarray.py      → fixed window example
longest_substring.py     → variable window example
min_window_substring.py  → advanced sliding window
fixed_window_examples.py → more practice
sliding_window_patterns.md → summary of patterns
```

By the end of this section, you will understand how to **process ranges efficiently using sliding windows**.
