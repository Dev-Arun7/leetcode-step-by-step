"""
What you will learn:
- How fast and slow pointers work
- How to remove duplicates from a sorted array
- How to modify an array in place

Problem:

Given a **sorted array**, remove duplicates in place.

Return the number of unique elements.

Example:

Input:
[1,1,2]

Output:
[1,2,_]

Return value:
2

Explanation:
The first 2 elements are unique.
The remaining elements do not matter.
"""


# ------------------------------------------------------------
# Brute Force Idea
# ------------------------------------------------------------
# Use a new list to store unique values.
#
# Time: O(n)
# Space: O(n)

def remove_duplicates_bruteforce(nums):

    if not nums:
        return 0

    unique = [nums[0]]

    for num in nums[1:]:
        if num != unique[-1]:
            unique.append(num)

    return unique


# ------------------------------------------------------------
# Two Pointer Approach
# ------------------------------------------------------------
# Idea:
#
# slow pointer → position of last unique element
# fast pointer → scans the array
#
# When we find a new value:
# move slow pointer and update the array

def remove_duplicates(nums):

    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):

        if nums[fast] != nums[slow]:

            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


# ------------------------------------------------------------
# Step-by-step example
# ------------------------------------------------------------
# nums = [1,1,2,2,3]
#
# slow = 0
#
# fast scans the array:
#
# fast=1 → nums[1]=1 → same as nums[0] → skip
#
# fast=2 → nums[2]=2 → different
#
# move slow to index 1
# place value there
#
# array becomes:
#
# [1,2,2,2,3]
#
# continue...


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# Fast pointer:
# scans the array
#
# Slow pointer:
# tracks the position of unique values
#
# This pattern is called:
#
# fast & slow pointers


# ------------------------------------------------------------
# Beginner Mistakes
# ------------------------------------------------------------
# 1. Forgetting that the array must be sorted
#
# 2. Returning the array instead of the count
#
# 3. Moving slow pointer too early
#
# 4. Forgetting that slow+1 is the length


# ------------------------------------------------------------
# Runnable Examples
# ------------------------------------------------------------
nums1 = [1,1,2]
print("Original:", nums1)

length = remove_duplicates(nums1)

print("New length:", length)
print("Unique elements:", nums1[:length])


nums2 = [0,0,1,1,1,2,2,3,3,4]
print("\nOriginal:", nums2)

length = remove_duplicates(nums2)

print("New length:", length)
print("Unique elements:", nums2[:length])


nums3 = [1,1,1,1]
print("\nOriginal:", nums3)

length = remove_duplicates(nums3)

print("New length:", length)
print("Unique elements:", nums3[:length])


# ------------------------------------------------------------
# Small Practice
# ------------------------------------------------------------
# 1. Return the list of unique values instead of the length
#
# 2. Count how many duplicates were removed
#
# 3. Modify the code to keep at most TWO duplicates
#
# Example:
# [1,1,1,2,2,3]
#
# Result:
# [1,1,2,2,3]
#
# 4. Try running this algorithm on an unsorted array
# and observe what happens.