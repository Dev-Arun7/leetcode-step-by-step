"""
max_sum_subarray.py

What you will learn:
- How a fixed-size sliding window works
- How to avoid recalculating sums repeatedly
- How sliding window improves efficiency

Problem:

Given an array and a number k,
find the maximum sum of any subarray of size k.

Example:

nums = [2,1,5,1,3,2]
k = 3

Subarrays of size 3:

[2,1,5] -> sum = 8
[1,5,1] -> sum = 7
[5,1,3] -> sum = 9
[1,3,2] -> sum = 6

Maximum sum = 9
"""


# ------------------------------------------------------------
# Brute Force Approach
# ------------------------------------------------------------
# Calculate the sum of every subarray of size k
#
# Time Complexity: O(n * k)

def max_sum_bruteforce(nums, k):

    max_sum = 0

    for i in range(len(nums) - k + 1):

        window_sum = 0

        for j in range(i, i + k):
            window_sum += nums[j]

        max_sum = max(max_sum, window_sum)

    return max_sum


# ------------------------------------------------------------
# Sliding Window Approach
# ------------------------------------------------------------
# Idea:
#
# Instead of recalculating every subarray sum,
# we reuse the previous window sum.
#
# When the window moves:
#
# subtract the left value
# add the new right value

def max_sum_sliding_window(nums, k):

    window_sum = 0
    max_sum = 0

    # First window
    for i in range(k):
        window_sum += nums[i]

    max_sum = window_sum

    # Slide the window
    for right in range(k, len(nums)):

        window_sum += nums[right]
        window_sum -= nums[right - k]

        max_sum = max(max_sum, window_sum)

    return max_sum


# ------------------------------------------------------------
# Step-by-step example
# ------------------------------------------------------------
# nums = [2,1,5,1,3,2]
# k = 3
#
# First window:
#
# [2,1,5] -> sum = 8
#
# Move window:
#
# remove 2
# add 1
#
# [1,5,1] -> sum = 7
#
# Move window:
#
# remove 1
# add 3
#
# [5,1,3] -> sum = 9
#
# Move window:
#
# remove 5
# add 2
#
# [1,3,2] -> sum = 6


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# Sliding window works because
# consecutive windows share many elements.
#
# Instead of recalculating everything,
# we only update what changed.


# ------------------------------------------------------------
# Beginner Mistakes
# ------------------------------------------------------------
# 1. Forgetting to subtract the element leaving the window
#
# window_sum -= nums[right - k]
#
# 2. Forgetting to initialize the first window
#
# 3. Using nested loops instead of sliding the window
#
# 4. Confusing window size with array size


# ------------------------------------------------------------
# Runnable Examples
# ------------------------------------------------------------
nums1 = [2,1,5,1,3,2]
k1 = 3

print("Array:", nums1)
print("k:", k1)

print("Brute force:", max_sum_bruteforce(nums1, k1))
print("Sliding window:", max_sum_sliding_window(nums1, k1))


nums2 = [4,2,1,7,8,1,2,8]
k2 = 3

print("\nArray:", nums2)
print("Sliding window:", max_sum_sliding_window(nums2, k2))


nums3 = [1,1,1,1,1]
k3 = 2

print("\nArray:", nums3)
print("Sliding window:", max_sum_sliding_window(nums3, k3))



# ------------------------------------------------------------
# Small Practice (Explained)
# ------------------------------------------------------------

# 1. Return the subarray that has the maximum sum
#
# Earlier we returned only the maximum sum.
# Now return the actual subarray that produced that sum.
#
# Example:
# nums = [2,1,5,1,3,2]
# k = 3
#
# Windows of size 3:
# [2,1,5] -> sum = 8
# [1,5,1] -> sum = 7
# [5,1,3] -> sum = 9   ← largest
# [1,3,2] -> sum = 6
#
# So the result should be:
# [5,1,3]


# 2. Find the minimum sum subarray of size k
#
# Instead of the largest sum,
# now find the window with the smallest sum.
#
# Example:
# nums = [2,1,5,1,3,2]
# k = 3
#
# Windows:
# [2,1,5] -> 8
# [1,5,1] -> 7
# [5,1,3] -> 9
# [1,3,2] -> 6  ← smallest
#
# Answer should be 6 (or the subarray [1,3,2]).


# 3. Find the average of each subarray of size k
#
# Instead of keeping only the maximum,
# compute the average for every window.
#
# Example:
# nums = [2,1,5,1,3,2]
# k = 3
#
# Windows:
# [2,1,5] -> sum = 8  -> average = 8/3
# [1,5,1] -> sum = 7  -> average = 7/3
# [5,1,3] -> sum = 9  -> average = 9/3
# [1,3,2] -> sum = 6  -> average = 6/3
#
# Result could be:
# [2.67, 2.33, 3.0, 2.0]


# 4. Count how many windows have sum greater than 10
#
# Instead of storing sums, count how many windows
# satisfy a condition.
#
# Example:
# nums = [2,5,3,8,1,2]
# k = 2
#
# Windows:
# [2,5] -> 7
# [5,3] -> 8
# [3,8] -> 11  ← greater than 10
# [8,1] -> 9
# [1,2] -> 3
#
# Only one window satisfies the condition.
#
# Answer: 1


# 5. Try solving the problem without sliding window
#
# Write the brute force version first.
#
# That means:
# - use nested loops
# - compute the sum of each window from scratch
#
# Compare the two approaches:
#
# Brute force time complexity:
# O(n * k)
#
# Sliding window time complexity:
# O(n)
#
# This helps you see why sliding window is powerful.