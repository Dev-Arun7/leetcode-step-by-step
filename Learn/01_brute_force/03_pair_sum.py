"""
What you learn:
- Brute force nested loop to find a pair
- How to avoid using the same element twice
- How to return early when you find an answer
- Better ways (two pointers after sorting, and set/hashmap style)

Where you use this:
- Classic LeetCode: Pair Sum / Two Sum
- Many problems reduce to "find two items that match a condition"

Problem:
Given a list of integers nums and an integer target,
return True if any two DIFFERENT elements add up to target, otherwise False.

Example:
nums = [2, 7, 11, 15], target = 9  -> True (2 + 7)
"""


# ------------------------------------------------------------
# Solution 1: Brute force (nested loops)
# Time: O(n^2), Space: O(1)
# ------------------------------------------------------------
def pair_sum_bruteforce(nums, target):
    # Check all pairs (i, j) with i < j
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False


# ------------------------------------------------------------
# Solution 2: Sorting + two pointers
# Time: O(n log n), Space: O(n) because sorted() makes a new list
# ------------------------------------------------------------
def pair_sum_two_pointers(nums, target):
    sorted_nums = sorted(nums)

    left = 0
    right = len(sorted_nums) - 1

    while left < right:
        current_sum = sorted_nums[left] + sorted_nums[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False


# ------------------------------------------------------------
# Solution 3: Using a set (fast, common in LeetCode)
# Time: O(n), Space: O(n)
# ------------------------------------------------------------
def pair_sum_set(nums, target):
    seen = set()

    for x in nums:
        needed = target - x

        # If we already saw the needed number, we found a pair
        if needed in seen:
            return True

        # Otherwise remember current number
        seen.add(x)

    return False


# ------------------------------------------------------------
# Run examples (so beginners can run this file directly)
# ------------------------------------------------------------
nums1 = [2, 7, 11, 15]
target1 = 9
print("nums:", nums1, "target:", target1)
print("Brute force:", pair_sum_bruteforce(nums1, target1))
print("Two pointers:", pair_sum_two_pointers(nums1, target1))
print("Set method:", pair_sum_set(nums1, target1))

nums2 = [1, 2, 3, 4]
target2 = 8
print("\nnums:", nums2, "target:", target2)
print("Brute force:", pair_sum_bruteforce(nums2, target2))
print("Two pointers:", pair_sum_two_pointers(nums2, target2))
print("Set method:", pair_sum_set(nums2, target2))

# Edge cases
nums3 = []
target3 = 5
print("\nnums:", nums3, "target:", target3)
print("Set method:", pair_sum_set(nums3, target3))

nums4 = [5]
target4 = 10
print("\nnums:", nums4, "target:", target4)
print("Set method:", pair_sum_set(nums4, target4))

nums5 = [3, 3]
target5 = 6
print("\nnums:", nums5, "target:", target5)
print("Set method:", pair_sum_set(nums5, target5))