"""
What you learn:
- How to compare elements in a list
- How to compare neighboring elements
- How to check if an array is sorted
- Basic comparison patterns used in many problems

Where this is used:
Comparison patterns appear in many problems:

Examples:
- Check if array is sorted
- Find increasing/decreasing patterns
- Detect duplicates in sorted arrays
- Compare neighbors in sliding window problems

Time Complexity:
O(n) because we scan the list once.
"""


# ------------------------------------------------------------
# Solution 1: Check if array is sorted (ascending)
# ------------------------------------------------------------
def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False

    return True


# ------------------------------------------------------------
# Solution 2: Find increasing pairs
# Example: (1,3), (3,5)
# ------------------------------------------------------------
def find_increasing_pairs(nums):
    pairs = []

    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            pairs.append((nums[i], nums[i + 1]))

    return pairs


# ------------------------------------------------------------
# Solution 3: Find decreasing pairs
# ------------------------------------------------------------
def find_decreasing_pairs(nums):
    pairs = []

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            pairs.append((nums[i], nums[i + 1]))

    return pairs


# ------------------------------------------------------------
# Solution 4: Compare two lists element by element
# ------------------------------------------------------------
def compare_lists(nums1, nums2):
    length = min(len(nums1), len(nums2))

    result = []

    for i in range(length):
        if nums1[i] == nums2[i]:
            result.append("equal")
        elif nums1[i] > nums2[i]:
            result.append("first bigger")
        else:
            result.append("second bigger")

    return result


# ------------------------------------------------------------
# Run examples
# ------------------------------------------------------------
nums = [1, 3, 5, 4, 6]

print("List:", nums)

print("\nIs sorted?")
print(is_sorted(nums))

print("\nIncreasing pairs:")
print(find_increasing_pairs(nums))

print("\nDecreasing pairs:")
print(find_decreasing_pairs(nums))


nums1 = [1, 5, 3]
nums2 = [1, 2, 3]

print("\nCompare two lists:")
print(compare_lists(nums1, nums2))