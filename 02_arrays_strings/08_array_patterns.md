# Array and String Patterns

## Prerequisites

Before learning array and string problems, you should know:

- Variables
- if / else
- for loops
- Lists
- Strings
- Functions
- Basic indexing

Example:

```python
nums = [10, 20, 30]
text = "hello"

print(nums[0])   # 10
print(text[1])   # e
```

---

## Why Arrays and Strings Matter

Arrays and strings are the most common starting point in LeetCode.

Many beginner problems are based on:

- traversing
- counting
- comparing
- reversing
- checking duplicates
- checking patterns

If you understand arrays and strings well,
many other topics become easier later.

---

## Common Array Patterns

### 1. Traversing

This means visiting each element one by one.

Example:

```python
for num in nums:
    print(num)
```

Used for:
- searching
- counting
- finding max/min
- updating answers while scanning

---

### 2. Using Index

Sometimes the value is not enough.
You also need the position.

Example:

```python
for i in range(len(nums)):
    print(i, nums[i])
```

Used for:
- comparing neighbors
- updating values
- checking previous/next element

---

### 3. Comparing Neighbors

A very common pattern:

```python
for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        print("Duplicate neighbors found")
```

Used for:
- sorted arrays
- duplicate detection
- increasing/decreasing checks

---

### 4. Reversing

Reversing is common in both arrays and strings.

Example:

```python
nums[::-1]
text[::-1]
```

Used for:
- palindrome checking
- reverse operations
- two pointer problems

---

### 5. Counting

Counting is one of the most important beginner skills.

Example:

```python
count = 0

for num in nums:
    if num == 2:
        count += 1
```

Used for:
- frequency problems
- duplicate problems
- string character counts

---

### 6. Tracking Best Answer

This means keeping the current best result while traversing.

Example:

```python
max_value = nums[0]

for num in nums:
    if num > max_value:
        max_value = num
```

Used for:
- max/min problems
- best score
- stock buy/sell
- maximum difference

---

## Common String Patterns

Strings are similar to arrays because you can traverse them too.

Example:

```python
text = "hello"

for char in text:
    print(char)
```

Common string patterns:
- reverse string
- palindrome check
- count characters
- compare characters
- substring problems

---

## Important Beginner Ideas

### Arrays and Strings are Ordered

Order matters.

Example:

```python
[1, 2, 3] != [3, 2, 1]
```

```python
"abc" != "cba"
```

That means position is often important.

---

### Strings are Immutable

In Python, strings cannot be changed directly.

Example:

```python
text = "hello"
# text[0] = "H"   # This will give an error
```

So in string problems, we often:
- build a new string
- use slicing
- use join()

---

### Lists are Mutable

Lists can be changed directly.

Example:

```python
nums = [1, 2, 3]
nums[0] = 10
print(nums)   # [10, 2, 3]
```

This is why some array solutions work in-place.

---

## How to Think in Array/String Problems

When you see an array or string problem, ask:

1. Do I need to traverse?
2. Do I need index or only value?
3. Am I counting something?
4. Am I comparing neighbors?
5. Do I need to reverse?
6. Do I need to track max/min?
7. Is sorting helpful?

These questions help you choose the right approach.

---

## Common Beginner Mistakes

### 1. Index Out of Range

Example:

```python
for i in range(len(nums)):
    print(nums[i + 1])
```

This can crash on the last index.

---

### 2. Forgetting Empty Input

Example:

```python
nums = []
max_value = nums[0]   # Error
```

Always think about edge cases.

---

### 3. Confusing List and String Behavior

Lists can be modified.
Strings cannot.

---

### 4. Using More Complex Logic Too Early

Start simple:
- loop
- compare
- count
- return answer

Then optimize later.

---

## Beginner Checklist for Array/String Problems

Before solving, ask:

- [ ] Do I understand the input?
- [ ] Do I need index or value?
- [ ] Can I solve it by one loop?
- [ ] Am I comparing neighbors?
- [ ] Do I need extra space?
- [ ] Did I test edge cases?

---

## Summary

Arrays and strings are the foundation of DSA problem solving.

Master these skills first:

- traversing
- reversing
- counting
- comparing
- finding duplicates
- finding max/min

These patterns appear again and again in harder topics later.

If your array and string basics are strong,
LeetCode becomes much easier.