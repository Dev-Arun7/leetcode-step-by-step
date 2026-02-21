# Complexity Basics (Big-O)

## Prerequisites

You should know:

- for loops
- nested loops
- Basic math (n, n²)

---

## What is Time Complexity?

Time complexity tells us:

> How the number of operations grows as input size grows.

We use Big-O notation.

---

## Common Complexities

### O(1) – Constant Time

Example:
Accessing one element in a list.

nums[0]

Always same time.

---

### O(n) – Linear Time

Example:

for x in nums:
    print(x)

If list doubles, time doubles.

---

### O(n²) – Quadratic Time

Example:

for i in range(n):
    for j in range(n):
        print(i, j)

If n doubles, work becomes 4 times bigger.

---

## Why It Matters

If n = 100,000:

O(n²) = 10,000,000,000 operations → too slow

That is why optimization matters.

---

## Space Complexity

Space complexity tells us:

> How much extra memory we use.

Examples:

- Using only a few variables → O(1)
- Creating new list of size n → O(n)
- Using dictionary/set storing n items → O(n)

---

## Beginner Rule

When you finish coding, always ask:

- What is time complexity?
- What is space complexity?