"""
What you learn:
- What the Two Sum problem is
- How to solve it using brute force
- How a hashmap makes the solution faster
- How to store visited numbers
- How to find the matching pair using complement

Where this is used:
Two Sum is one of the most famous hashmap problems.

Examples:
- Find two numbers that add to a target
- Store seen values
- Check if a matching value already exists
- Build fast lookup solutions

Problem:
Given a list of numbers and a target,
return the indices of two numbers whose sum is equal to target.

Example:
nums = [2, 7, 11, 15]
target = 9

Answer:
[0, 1]

Because:
nums[0] + nums[1] = 2 + 7 = 9
"""


# ------------------------------------------------------------
# Solution 1: Brute Force
# ------------------------------------------------------------
# Check every pair.
# This is simple and good for learning.
#
# Time: O(n^2)
# Space: O(1)

def two_sum_bruteforce(nums, target):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


# ------------------------------------------------------------
# Solution 2: Hashmap / Dictionary
# ------------------------------------------------------------
# Idea:
# For each number, calculate:
# needed = target - current number
#
# Then check:
# Have we already seen this needed value?
#
# If yes, we found the answer.
#
# Dictionary stores:
# number -> index
#
# Time: O(n)
# Space: O(n)

def two_sum_hashmap(nums, target):

    seen = {}

    for i in range(len(nums)):
        current_num = nums[i]
        needed = target - current_num

        if needed in seen:
            return [seen[needed], i]

        seen[current_num] = i

    return []


# ------------------------------------------------------------
# Solution 3: Same hashmap idea with enumerate()
# ------------------------------------------------------------
# This is slightly cleaner, but still beginner friendly.

def two_sum_hashmap_enumerate(nums, target):

    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i

    return []


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# The most important idea in Two Sum is:
#
# needed = target - current_num
#
# Instead of asking:
# "Which two numbers add to target?"
#
# We ask:
# "For this current number, what other number do I need?"
#
# Example:
#
# nums = [2, 7, 11, 15]
# target = 9
#
# First number = 2
# needed = 9 - 2 = 7
#
# Have we seen 7 already?
# No
#
# Store 2 in dictionary
#
# Next number = 7
# needed = 9 - 7 = 2
#
# Have we seen 2 already?
# Yes
#
# So answer is the index of 2 and the current index of 7
#
# This pattern is very important in many problems:
# - Two Sum
# - Pair problems
# - Difference problems
# - Seen-value problems
#
# When you see:
# "find a pair"
# "check if matching value exists"
# think:
# "can I use a hashmap?"


# ------------------------------------------------------------
# Common Beginner Mistakes
# ------------------------------------------------------------
# 1. Storing index first, then checking
#
#    Wrong order can cause issues in some cases.
#    First check if needed value exists.
#    Then store the current number.
#
# 2. Returning numbers instead of indices
#
#    This problem usually asks for indices, not values.
#
# 3. Using the same element twice
#
#    Example:
#    nums = [3, 3], target = 6
#
#    We need two different positions.
#
# 4. Forgetting what dictionary stores
#
#    In this solution:
#    number -> index
#
# 5. Confusing value and index
#
#    nums[i] is value
#    i is index


# ------------------------------------------------------------
# Run examples
# ------------------------------------------------------------
nums1 = [2, 7, 11, 15]
target1 = 9

print("Nums:", nums1)
print("Target:", target1)

print("\nSolution 1 (brute force):")
print(two_sum_bruteforce(nums1, target1))

print("\nSolution 2 (hashmap):")
print(two_sum_hashmap(nums1, target1))

print("\nSolution 3 (hashmap + enumerate):")
print(two_sum_hashmap_enumerate(nums1, target1))


nums2 = [3, 2, 4]
target2 = 6

print("\nNums:", nums2)
print("Target:", target2)
print("Brute force:", two_sum_bruteforce(nums2, target2))
print("Hashmap:", two_sum_hashmap(nums2, target2))


nums3 = [3, 3]
target3 = 6

print("\nNums:", nums3)
print("Target:", target3)
print("Brute force:", two_sum_bruteforce(nums3, target3))
print("Hashmap:", two_sum_hashmap(nums3, target3))


# Edge cases
nums4 = []
target4 = 5

print("\nNums:", nums4)
print("Target:", target4)
print("Hashmap:", two_sum_hashmap(nums4, target4))


nums5 = [1]
target5 = 2

print("\nNums:", nums5)
print("Target:", target5)
print("Hashmap:", two_sum_hashmap(nums5, target5))


# ------------------------------------------------------------
# Small Practice
# ------------------------------------------------------------
# Try modifying this code to solve these:
#
# 1. Return the values instead of indices
#    Example:
#    [2, 7, 11, 15], target = 9 -> [2, 7]
#
# 2. Count how many pairs give the target
#
# 3. Check if any pair exists
#    Return True or False
#
# 4. Solve Two Sum in a sorted array
#    Can you do it with two pointers instead of hashmap?