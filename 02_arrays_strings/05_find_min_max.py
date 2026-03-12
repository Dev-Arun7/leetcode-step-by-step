"""
What you learn:
- How to find minimum and maximum values in a list
- How to track multiple values during traversal
- One-pass vs two-pass approaches
- Python shortcuts for the same problem

Where this is used:
Many problems require tracking extremes:

Examples:
- Find largest/smallest value
- Stock buy/sell problems
- Range calculations
- Finding best/worst score

Time Complexity:
Most methods are O(n) because we scan the list once.
"""


# ------------------------------------------------------------
# Solution 1: Find min and max using one loop
# Time: O(n), Space: O(1)
# ------------------------------------------------------------
def find_min_max(nums):

    if len(nums) == 0:
        return None

    min_value = nums[0]
    max_value = nums[0]

    for num in nums:
        if num < min_value:
            min_value = num

        if num > max_value:
            max_value = num

    return min_value, max_value


# ------------------------------------------------------------
# Solution 2: Two separate loops
# Time: O(n) + O(n) = O(n)
# ------------------------------------------------------------
def find_min_max_two_loops(nums):

    if len(nums) == 0:
        return None

    min_value = nums[0]
    max_value = nums[0]

    for num in nums:
        if num < min_value:
            min_value = num

    for num in nums:
        if num > max_value:
            max_value = num

    return min_value, max_value


# ------------------------------------------------------------
# Solution 3: Python built-in functions
# Time: O(n)
# ------------------------------------------------------------
def find_min_max_builtin(nums):

    if len(nums) == 0:
        return None

    return min(nums), max(nums)


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# This pattern is very important:
#
# min_value = nums[0]
# max_value = nums[0]
#
# Then updating them while traversing the list.
#
# This idea appears in many problems:
# - Best time to buy and sell stock
# - Maximum difference in array
# - Tracking minimum prefix values
# - Finding best or worst score
#
# Key concept:
# "Keep updating the best answer while scanning the array"


# ------------------------------------------------------------
# Run examples
# ------------------------------------------------------------
nums = [5, 2, 9, 1, 7]

print("List:", nums)

print("\nSolution 1 (one loop):")
print(find_min_max(nums))

print("\nSolution 2 (two loops):")
print(find_min_max_two_loops(nums))

print("\nSolution 3 (built-in):")
print(find_min_max_builtin(nums))


# Edge cases
nums2 = [-5, -10, -1]
print("\nList:", nums2)
print(find_min_max(nums2))

nums3 = []
print("\nList:", nums3)
print(find_min_max(nums3))