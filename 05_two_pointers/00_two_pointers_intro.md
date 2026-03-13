# Two Pointers Introduction

The **two pointer technique** is a very powerful method used to solve many array and string problems efficiently.

Instead of using **nested loops**, we use **two indices (pointers)** that move through the data.

Typical structure:

```
left pointer
right pointer
```

By moving these pointers intelligently, we can often reduce a problem from:

```
O(n²)
```

to:

```
O(n)
```

---

# Basic Idea

Imagine a list:

```
[1, 2, 3, 4, 5]
```

We can place two pointers like this:

```
L           R
1  2  3  4  5
```

Then move them depending on the condition.

Example moves:

```
L → move right
R ← move left
```

This allows us to explore combinations **without checking every pair**.

---

# Example: Pair Sum in a Sorted Array

Problem:

Find two numbers that add up to a target.

Example:

```
nums = [1, 2, 4, 6, 8]
target = 10
```

Start with:

```
L           R
1  2  4  6  8
```

Check:

```
1 + 8 = 9
```

Too small → move left pointer.

```
   L        R
1  2  4  6  8
```

Now:

```
2 + 8 = 10
```

Found the answer.

No nested loops needed.

---

# Common Two Pointer Patterns

Two pointers are commonly used for:

* pair problems
* removing duplicates
* reversing arrays
* palindromes
* container problems
* sliding windows

---

# Pattern 1 — Opposite Ends

Pointers start from both ends.

```
L           R
1  2  3  4  5
```

Used for:

* pair sum
* reversing arrays
* palindrome checking

---

# Pattern 2 — Fast and Slow Pointers

Two pointers move at **different speeds**.

Example:

```
slow pointer
fast pointer
```

Used for:

* removing duplicates
* linked list cycle detection

---

# Pattern 3 — Expanding Window

Pointers create a **range**.

```
L     R
1  2  3  4  5
```

Used for:

* substring problems
* window problems

(This leads to the **sliding window technique** later.)

---

# When Should You Think About Two Pointers?

Consider two pointers when a problem involves:

* sorted arrays
* pair problems
* comparing both ends
* removing duplicates
* scanning ranges

Ask yourself:

```
Can two pointers replace nested loops?
```

If yes, the problem may become much faster.

---

# Time Complexity Advantage

Without two pointers:

```
O(n²)
```

With two pointers:

```
O(n)
```

This is a huge improvement for large inputs.

---

# What You Will Learn Next

In this section:

```
pair_sum_sorted.py          → find pairs in sorted arrays
remove_duplicates.py        → remove duplicates using pointers
container_with_most_water.py → classic two pointer problem
reverse_string.py           → reverse using two pointers
two_pointers_patterns.md    → summary of patterns
```

By the end of this section you will be able to recognize when **two pointers can turn a slow solution into a fast one**.
