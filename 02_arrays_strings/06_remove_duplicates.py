"""
What you learn:
- How to remove duplicates from a list
- Different ways to solve the same problem
- Brute force approach
- Using a set
- Sorting and comparing neighbors

Where this is used:
Removing duplicates is common in many problems.

Examples:
- Cleaning repeated data
- Finding unique elements
- Preparing arrays for other operations
- Many LeetCode problems

Example:
Input:
[1, 2, 2, 3, 4, 4, 5]

Output:
[1, 2, 3, 4, 5]
"""


# ------------------------------------------------------------
# Solution 1: Brute Force
# ------------------------------------------------------------
# Idea:
# Create a new list.
# Add a number only if it is not already present.

def remove_duplicates_bruteforce(nums):

    result = []

    for num in nums:
        if num not in result:
            result.append(num)

    return result


# ------------------------------------------------------------
# Solution 2: Using a Set
# ------------------------------------------------------------
# A set automatically removes duplicates.
# Note: Order may change.

def remove_duplicates_set(nums):

    return list(set(nums))


# ------------------------------------------------------------
# Solution 3: Sorting and comparing neighbors
# ------------------------------------------------------------
# Sort the list first.
# Duplicate values become neighbors.
# Then keep only values that are different from the previous one.

def remove_duplicates_sort(nums):

    if len(nums) == 0:
        return []

    sorted_nums = sorted(nums)

    result = [sorted_nums[0]]

    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] != sorted_nums[i - 1]:
            result.append(sorted_nums[i])

    return result


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# This pattern is very important:
#
# if sorted_nums[i] != sorted_nums[i - 1]
#
# After sorting, duplicate values come next to each other.
#
# This idea appears in many problems:
# - Remove duplicates
# - Detect duplicates
# - Count unique values
# - Compare neighbors in sorted arrays


# ------------------------------------------------------------
# Common Beginner Mistakes
# ------------------------------------------------------------
# 1. Forgetting that set() may change the order
#
# 2. Comparing neighbors without sorting first
#
# 3. Using nums[i + 1] carelessly and getting index errors


# ------------------------------------------------------------
# Run examples
# ------------------------------------------------------------
nums = [1, 2, 2, 3, 4, 4, 5]

print("Original list:", nums)

print("\nSolution 1 (brute force):")
print(remove_duplicates_bruteforce(nums))

print("\nSolution 2 (set):")
print(remove_duplicates_set(nums))

print("\nSolution 3 (sorting):")
print(remove_duplicates_sort(nums))


# Edge cases
nums2 = []
print("\nEmpty list:", remove_duplicates_bruteforce(nums2))

nums3 = [5, 5, 5, 5]
print("\nAll duplicates:", remove_duplicates_bruteforce(nums3))


# ------------------------------------------------------------
# Small Practice
# ------------------------------------------------------------
# Try modifying this code to solve these:
#
# 1. Remove duplicates from a string
#    Example: "banana" -> "ban"
#
# 2. Count how many unique numbers exist in a list
#
# 3. Return duplicates only
#    Example: [1,2,2,3,3,4] -> [2,3]