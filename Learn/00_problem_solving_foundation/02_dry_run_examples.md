# Dry Run Examples

## Prerequisites

You should know:

- for loops
- if statements
- How to trace code manually

---

## What is a Dry Run?

Dry run means:

> Manually run your code on paper step by step.

This helps you:
- Find logical errors
- Understand your own solution
- Build confidence

---

## Example 1: Find Maximum

Input:
nums = [3, 1, 5, 2]

Algorithm:
1. max_value = nums[0] → 3
2. Compare with 1 → no change
3. Compare with 5 → update to 5
4. Compare with 2 → no change
5. Return 5

Dry running shows how the value changes.

---

## Example 2: Pair Sum

nums = [2, 7, 11, 15]
target = 9

Nested loop:

i=0 → 2  
j=1 → 7 → 2+7=9 → Found True

Stop early.

Dry run helps you see:
- How loops move
- When conditions become true

---

## Why Beginners Skip Dry Run (Mistake)

Many beginners:
- Code fast
- Test once
- Move on

Instead:
Always dry run at least one example manually.

---

## Beginner Rule

If your solution is not working:

Dry run it slowly.

Check:
- Loop values
- Variable updates
- Condition checks