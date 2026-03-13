"""
What you will learn:
- How the two pointer technique works
- How to find a pair of numbers that sum to a target
- How to replace nested loops with two pointers

Problem:

Given a **sorted array**, find two numbers that add up to a target value.

Example:

nums = [1, 2, 4, 6, 8]
target = 10

Answer:
[2, 8]

Important:
This technique works best when the array is **already sorted**.
"""


# ------------------------------------------------------------
# Brute Force Approach
# ------------------------------------------------------------
# Check every pair using nested loops.
#
# Time Complexity: O(n²)

def pair_sum_bruteforce(nums, target):

    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):

            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]

    return None


# ------------------------------------------------------------
# Two Pointer Approach
# ------------------------------------------------------------
# Idea:
#
# One pointer starts from the left.
# One pointer starts from the right.
#
# If sum is too small → move left pointer right
# If sum is too large → move right pointer left

def pair_sum_two_pointers(nums, target):

    left = 0
    right = len(nums) - 1

    while left < right:

        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [nums[left], nums[right]]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return None


# ------------------------------------------------------------
# Step-by-step example
# ------------------------------------------------------------
# nums = [1,2,4,6,8]
# target = 10
#
# L           R
# 1  2  4  6  8
#
# 1 + 8 = 9 (too small)
#
# move L →
#
#    L        R
# 1  2  4  6  8
#
# 2 + 8 = 10
#
# pair found


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# Two pointers work well because the array is sorted.
#
# If sum is too small:
# move left pointer → increases sum
#
# If sum is too large:
# move right pointer → decreases sum
#
# This avoids checking every pair.


# ------------------------------------------------------------
# Beginner Mistakes
# ------------------------------------------------------------
# 1. Using two pointers on an unsorted array
#
# This technique assumes the array is sorted.
#
# 2. Forgetting the condition:
#
# while left < right
#
# 3. Moving both pointers at the same time
#
# Only move the pointer that helps adjust the sum.


# ------------------------------------------------------------
# Runnable Examples
# ------------------------------------------------------------
nums1 = [1, 2, 4, 6, 8]
target1 = 10

print("Array:", nums1)
print("Target:", target1)

print("Brute force:", pair_sum_bruteforce(nums1, target1))
print("Two pointers:", pair_sum_two_pointers(nums1, target1))


nums2 = [2, 3, 5, 7, 11]
target2 = 9

print("\nArray:", nums2)
print("Target:", target2)
print("Two pointers:", pair_sum_two_pointers(nums2, target2))


nums3 = [1, 3, 4, 5, 9]
target3 = 8

print("\nArray:", nums3)
print("Target:", target3)
print("Two pointers:", pair_sum_two_pointers(nums3, target3))


# ------------------------------------------------------------
# Small Practice
# ------------------------------------------------------------
# 1. Return the indices instead of the numbers
#
# Example:
# [1,2,4,6,8], target=10
#
# Answer:
# [1,4]
#
#
# 2. Count how many pairs equal the target
#
#
# 3. Return all pairs that equal the target
#
#
# 4. Try running the algorithm on an unsorted array
# and observe what happens.
#
#
# 5. Modify the code to return True/False
# if a pair exists.