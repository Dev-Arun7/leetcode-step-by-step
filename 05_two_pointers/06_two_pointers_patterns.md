# Two Pointers Patterns

The **two pointer technique** is used to scan arrays or strings using two indices instead of nested loops.

This often reduces a solution from:

```
O(n²)
```

to:

```
O(n)
```

Instead of checking every pair of elements, we move **two pointers** through the data in a smart way.

---

# Pattern 1 — Opposite Ends

Two pointers start at **both ends of the array**.

```
L           R
1  2  3  4  5
```

Depending on the condition, we move one of them.

Example moves:

```
L → move right
R ← move left
```

### Example Problems

* Pair sum in sorted array
* Container with most water
* Reverse string
* Palindrome checking

### Example idea

```python
left = 0
right = len(nums) - 1

while left < right:
    # process elements

    left += 1
    right -= 1
```

### Files in this repo

```
pair_sum_sorted.py
reverse_string.py
container_with_most_water.py
```

---

# Pattern 2 — Fast and Slow Pointers

Two pointers move **at different speeds**.

```
slow pointer
fast pointer
```

The slow pointer usually tracks **useful positions** while the fast pointer scans the list.

Example:

```
[1,1,2,2,3]
 S
 F
```

When fast finds a new value, slow moves forward.

### Example Problems

* Remove duplicates from sorted array
* Detect cycle in linked list
* Move zeroes

### Example idea

```python
slow = 0

for fast in range(len(nums)):
    
    if nums[fast] != nums[slow]:
        slow += 1
        nums[slow] = nums[fast]
```

### File in this repo

```
remove_duplicates.py
```

---

# Pattern 3 — Expand and Shrink

Two pointers define a **range (window)**.

```
L     R
1  2  3  4  5
```

We expand or shrink the window depending on the condition.

Example moves:

```
R → expand window
L → shrink window
```

This pattern is used heavily in **sliding window problems**.

### Example Problems

* Longest substring
* Maximum subarray
* Minimum window substring

(This technique will be explored in the **Sliding Window section**.)

---

# Pattern 4 — Move the Limiting Pointer

Sometimes one pointer limits the result.

Example:

**Container With Most Water**

Area depends on:

```
width * min(height_left, height_right)
```

The **shorter height limits the area**.

So we move the pointer pointing to the shorter line.

### File in this repo

```
container_with_most_water.py
```

---

# When Should You Think About Two Pointers?

Two pointers are often useful when the problem involves:

* sorted arrays
* pairs of elements
* comparing both ends
* removing duplicates
* reversing sequences
* scanning ranges

Ask yourself:

```
Can two pointers replace nested loops?
```

If yes, the algorithm may become much faster.

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

This improvement becomes very important for large inputs.

---

# Quick Pattern Cheat Sheet

| Pattern          | Idea                               | Example              |
| ---------------- | ---------------------------------- | -------------------- |
| Opposite Ends    | Start pointers at both ends        | Pair Sum             |
| Fast & Slow      | Pointers move at different speeds  | Remove Duplicates    |
| Expand / Shrink  | Maintain a range                   | Sliding Window       |
| Limiting Pointer | Move the value limiting the result | Container With Water |

---

# Key Takeaway

Two pointers are not just a trick.

They are a **way to scan data efficiently**.

Most two pointer solutions follow this idea:

```
1. Initialize two pointers
2. Move pointers based on a condition
3. Continue until pointers meet
```

Learning to recognize this pattern will help solve many array and string problems efficiently.
