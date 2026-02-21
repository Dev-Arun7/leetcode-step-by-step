"""
What you learn:
- How to find duplicates using brute force (nested loops)
- Why nested loops can become slow for large inputs
- Better ways using sorting or a set (hashing)
- How to build result step-by-step in a beginner-friendly way

Where you use this:
- Checking repeated elements in arrays
- Removing duplicates
- Frequency / counting problems (later with hashmap)

Problem:
Given a list of integers, return the duplicate values.

Examples:
nums = [1, 2, 3, 2, 4, 1]
duplicates -> [1, 2]   (order can vary depending on solution)

Note:
There are multiple correct ways.
We'll include a beginner brute-force way first, then better ways.
"""


# ------------------------------------------------------------
# Solution 1: Brute force (nested loops)
# Time: O(n^2), Space: O(k) for duplicates list
# ------------------------------------------------------------
def find_duplicates_bruteforce(nums):
    duplicates = []

    # Compare each number with every number after it
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):

            # If they match, nums[i] is a duplicate value
            if nums[i] == nums[j]:

                # Avoid adding the same duplicate multiple times
                if nums[i] not in duplicates:
                    duplicates.append(nums[i])

    return duplicates

"""
Note:
In Solution 1, we used: if nums[i] not in duplicates:
That check itself is a loop, but duplicates list is usually small,
so it’s okay for learning.
"""


# ------------------------------------------------------------
# Solution 2: Using sorting (easier idea: duplicates become neighbors)
# Time: O(n log n), Space: O(n) because sorted() makes a new list
# ------------------------------------------------------------
def find_duplicates_sorting(nums):
    duplicates = []

    sorted_nums = sorted(nums)

    # Check neighbors only
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i - 1]:
            if sorted_nums[i] not in duplicates:
                duplicates.append(sorted_nums[i])

    return duplicates


# ------------------------------------------------------------
# Solution 3: Using a set (best for speed + common in LeetCode)
# Time: O(n), Space: O(n)
# ------------------------------------------------------------
def find_duplicates_set(nums):
    seen = set()
    duplicates = []

    for x in nums:
        # If x already seen, it's a duplicate
        if x in seen:
            if x not in duplicates:
                duplicates.append(x)
        else:
            seen.add(x)

    return duplicates


# ------------------------------------------------------------
# Run examples (so beginners can run this file directly)
# ------------------------------------------------------------
nums = [1, 2, 3, 2, 4, 1, 1, 5, 2]
print("List:", nums)

result1 = find_duplicates_bruteforce(nums)
print("Solution 1 (brute force nested loops):", result1)

result2 = find_duplicates_sorting(nums)
print("Solution 2 (sorting neighbors):", result2)

result3 = find_duplicates_set(nums)
print("Solution 3 (set seen values):", result3)

# Edge cases
nums2 = [1, 2, 3, 4]
print("\nList:", nums2)
print("Duplicates:", find_duplicates_set(nums2))  # []

nums3 = []
print("\nList:", nums3)
print("Duplicates:", find_duplicates_set(nums3))  # []