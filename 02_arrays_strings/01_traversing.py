"""
What you learn:
- How to traverse (scan) an array / list
- Different ways to loop through a list in Python
- When to use index vs value
- Basic patterns used in many LeetCode problems

Where this is used:
Almost every array/string problem requires traversing.

Examples:
- counting values
- searching
- comparing neighbors
- updating results while looping

Time Complexity:
O(n) because we visit each element once
"""


# ------------------------------------------------------------
# Method 1: Traverse using index
# ------------------------------------------------------------
def traverse_using_index(nums):
    print("Traverse using index")

    for i in range(len(nums)):
        print("Index:", i, "Value:", nums[i])


# ------------------------------------------------------------
# Method 2: Traverse using direct value
# ------------------------------------------------------------
def traverse_using_value(nums):
    print("Traverse using value")

    for num in nums:
        print("Value:", num)


# ------------------------------------------------------------
# Method 3: Traverse using index and value together
# enumerate() is useful when we need both
# ------------------------------------------------------------
def traverse_using_enumerate(nums):
    print("Traverse using enumerate")

    for index, value in enumerate(nums):
        print("Index:", index, "Value:", value)


# ------------------------------------------------------------
# Method 4: Reverse traversal
# ------------------------------------------------------------
def traverse_reverse(nums):
    print("Traverse in reverse")

    for i in range(len(nums) - 1, -1, -1):
        print("Index:", i, "Value:", nums[i])


# ------------------------------------------------------------
# Method 5: Traverse neighbors
# Useful when comparing current element with next
# ------------------------------------------------------------
def traverse_neighbors(nums):
    print("Traverse neighbors")

    for i in range(len(nums) - 1):
        print(nums[i], "and", nums[i + 1])


# ------------------------------------------------------------
# Run examples
# ------------------------------------------------------------
nums = [10, 20, 30, 40]

print("List:", nums)
print()

traverse_using_index(nums)
print()

traverse_using_value(nums)
print()

traverse_using_enumerate(nums)
print()

traverse_reverse(nums)
print()

traverse_neighbors(nums)