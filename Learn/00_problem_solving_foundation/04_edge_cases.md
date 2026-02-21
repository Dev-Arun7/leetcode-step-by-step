# Edge Cases

## Prerequisites

You should know:

- Lists
- Conditions
- How functions return values

---

## What Are Edge Cases?

Edge cases are unusual or extreme inputs.

They often break beginner code.

---

## Common Edge Cases in LeetCode

### 1. Empty Input

nums = []

What should you return?

---

### 2. Single Element

nums = [5]

Does your loop handle this correctly?

---

### 3. All Same Values

nums = [2, 2, 2, 2]

Some duplicate solutions break here.

---

### 4. Negative Numbers

nums = [-5, -2, -10]

Make sure comparisons still work.

---

### 5. Large Input

n = 100000

Will your solution be too slow?

---

## Why Edge Cases Matter

Many LeetCode submissions fail because:

- They didn’t test empty input
- They didn’t test single element
- They assumed positive numbers only

---

## Beginner Habit

Before submitting:

Test your solution with:

- []
- [1]
- [1, 1, 1]
- Negative numbers

Always test edge cases.