# Brute Force Patterns

## What is Brute Force?

Brute force means:

> Try every possible option and check which one works.

It is the most straightforward way to solve a problem.

No clever tricks.  
No optimization.  
Just check everything.

---

## Why Learn Brute Force First?

Many beginners try to jump directly to “optimal” solutions.

That causes:
- confusion
- frustration
- quitting early

Instead:

1. First solve it with brute force.
2. Make sure it works.
3. Then improve it.

Even experienced engineers start with brute force to understand the problem clearly.

---

## Common Brute Force Patterns

### 1) Single Loop (O(n))

Used when:
- scanning a list
- finding max / min
- counting something
- checking a condition

Example:

```python
for x in nums:
    # update answer
```

Common problems:
- Find maximum
- Count occurrences
- Check if a value exists
- Find smallest number

---

### 2) Nested Loops (O(n²))

Used when:
- comparing every pair
- finding duplicates
- checking all combinations of two elements

Example:

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        # compare nums[i] and nums[j]
```

Common problems:
- Pair sum (brute force)
- Duplicate detection
- Compare every element with others

---

### 3) Triple Nested Loops (O(n³))

Used when:
- checking all triplets
- testing combinations of 3 elements

Example:

```python
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # check triplet
```

Usually too slow for large inputs.

---

## Understanding Time Complexity

If you see:

- One loop → usually O(n)
- Two nested loops → usually O(n²)
- Three nested loops → usually O(n³)

This matters because:

If n = 100,000  
Then O(n²) = 10,000,000,000 operations → too slow.

---

## When Is Brute Force OK?

Brute force is fine when:

- Input size is small (n <= 1000)
- Interview says constraints are small
- You are still learning
- You want to deeply understand the problem

---

## When Brute Force Is Too Slow

If:

- n = 100,000
- n = 1,000,000

Then O(n²) will likely fail.

That is when we learn:
- Hashmaps
- Two pointers
- Sliding window
- Binary search
- Dynamic programming

But only AFTER understanding brute force.

---

## Important Beginner Rule

If you cannot solve it with brute force,
you probably do not fully understand the problem.

Start simple.
Then improve.

---

## Brute Force Checklist

Before optimizing, ask yourself:

- [ ] Does my brute force solution work?
- [ ] Did I test edge cases?
- [ ] What is the time complexity?
- [ ] Why might it be slow?

If you can answer these questions,
you are ready to optimize your solution.

---

## Summary

Brute force is not "bad".
It is the foundation of problem solving.

Every optimized solution starts from a brute force idea.

Master this first.
Then optimization becomes easy.