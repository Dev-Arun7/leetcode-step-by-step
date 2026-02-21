"""
What you learn:
- How to scan a list (brute force traversal)
- How to keep and update a "best so far" value
- Different ways to solve the same problem in Python
- Time and space comparison in simple words

Where you use this:
- Any time you must find the "best" value while looping:
  max/min, best score, largest/smallest, etc.

Problem:
Given a list of integers, return the maximum value.

Note:
Python already has max(nums), but we still learn the loop method because
many LeetCode problems use the same idea: "update answer while scanning".

Common beginner mistake:
- Starting loop from index 0 again (which re-checks the first value)
"""


# ------------------------------------------------------------
# Solution 1: Beginner method (for loop + index)
# Best for learning + efficient (no extra memory)
# Time: O(n), Space: O(1)
# ------------------------------------------------------------
def find_max_loop_index(nums):
    # If list is empty, no max value exists
    if len(nums) == 0:
        return None

    # Assume first number is the maximum
    max_value = nums[0]

    # Start from index 1 because index 0 is already used
    for i in range(1, len(nums)):
        # Compare current number with max_value
        if nums[i] > max_value:
            # Update max_value
            max_value = nums[i]

    return max_value


# ------------------------------------------------------------
# Solution 2: Beginner + clean (for loop + slicing)
# Easy to read, but slicing creates a NEW list (extra memory)
# Time: O(n), Space: O(n) because nums[1:] creates a copy
# ------------------------------------------------------------
def find_max_loop_slice(nums):
    if len(nums) == 0:
        return None

    max_value = nums[0]

    # nums[1:] creates a new list, so it's extra memory
    for x in nums[1:]:
        if x > max_value:
            max_value = x

    return max_value


# ------------------------------------------------------------
# Solution 3: Python shortcut (built-in max)
# Best in real projects
# Time: O(n), Space: O(1)
# ------------------------------------------------------------
def find_max_builtin(nums):
    if len(nums) == 0:
        return None

    return max(nums)


# ------------------------------------------------------------
# Solution 4: Sorting method (works but slower)
# Not recommended for just finding max
# Time: O(n log n), Space: O(n) because sorted() creates a new list
# ------------------------------------------------------------
def find_max_sort(nums):
    if len(nums) == 0:
        return None

    sorted_nums = sorted(nums)
    return sorted_nums[-1]


# ------------------------------------------------------------
# Run examples (so beginners can run this file directly)
# ------------------------------------------------------------
nums = [1, 2, 3, 4, 5, 6]
print("List:", nums)

result1 = find_max_loop_index(nums)
print("Solution 1 (loop + index):", result1)

result2 = find_max_loop_slice(nums)
print("Solution 2 (loop + slice):", result2)

result3 = find_max_builtin(nums)
print("Solution 3 (built-in max):", result3)

result4 = find_max_sort(nums)
print("Solution 4 (sorting):", result4)

# Edge case example
empty_nums = []
print("\nEmpty list:", empty_nums)
print("Solution 1:", find_max_loop_index(empty_nums))
print("Solution 2:", find_max_loop_slice(empty_nums))
print("Solution 3:", find_max_builtin(empty_nums))
print("Solution 4:", find_max_sort(empty_nums))