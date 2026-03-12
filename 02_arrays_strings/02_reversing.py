"""
What you learn:
- How to reverse a list or string
- Multiple ways to solve the same problem
- When to use loops vs Python shortcuts
- Introduction to the two-pointer technique

Where this is used:
Reversing appears in many problems:
- Palindrome checking
- String manipulation
- Two pointer techniques
- Stack-like operations

Time Complexity:
Most methods here are O(n) because we process each element once.
"""


# ------------------------------------------------------------
# Solution 1: Build a new reversed list using a loop
# Time: O(n), Space: O(n)
# ------------------------------------------------------------
def reverse_using_loop(nums):
    reversed_list = []

    # Traverse from the end to the beginning
    for i in range(len(nums) - 1, -1, -1):
        reversed_list.append(nums[i])

    return reversed_list


# ------------------------------------------------------------
# Solution 2: Two pointers (in-place reverse)
# Time: O(n), Space: O(1)
# ------------------------------------------------------------
def reverse_two_pointers(nums):
    left = 0
    right = len(nums) - 1

    # Swap elements until pointers meet
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]

        left += 1
        right -= 1

    return nums


# ------------------------------------------------------------
# Solution 3: Python slicing shortcut
# Time: O(n), Space: O(n)
# ------------------------------------------------------------
def reverse_using_slice(nums):
    return nums[::-1]


# ------------------------------------------------------------
# Solution 4: Using built-in reverse()
# This modifies the original list
# Time: O(n), Space: O(1)
# ------------------------------------------------------------
def reverse_using_builtin(nums):
    nums.reverse()
    return nums


# ------------------------------------------------------------
# Run examples
# ------------------------------------------------------------
nums = [1, 2, 3, 4, 5]

print("Original list:", nums)

print("\nSolution 1 (loop):")
print(reverse_using_loop(nums))

print("\nSolution 2 (two pointers):")
print(reverse_two_pointers(nums.copy()))

print("\nSolution 3 (slicing):")
print(reverse_using_slice(nums))

print("\nSolution 4 (built-in reverse):")
print(reverse_using_builtin(nums.copy()))


# Example with string
string_value = "hello"
print("\nOriginal string:", string_value)
print("Reversed string:", string_value[::-1])