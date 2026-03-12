"""
What you learn:
- How to count elements in a list
- How to count occurrences of a specific value
- How to count using loops and Python shortcuts
- Introduction to frequency counting

Where this is used:
Many problems require counting:

Examples:
- Count how many times a value appears
- Find most frequent element
- Count characters in a string
- Frequency based problems

Time Complexity:
Most counting methods are O(n) because we scan the list once.
"""


# ------------------------------------------------------------
# Solution 1: Count occurrences of a specific value using loop
# Time: O(n), Space: O(1)
# ------------------------------------------------------------
def count_value_loop(nums, target):
    count = 0

    for num in nums:
        if num == target:
            count += 1

    return count


# ------------------------------------------------------------
# Solution 2: Python built-in count()
# Time: O(n)
# ------------------------------------------------------------
def count_value_builtin(nums, target):
    return nums.count(target)


# ------------------------------------------------------------
# Solution 3: Count all values (frequency dictionary)
# Time: O(n), Space: O(n)
# ------------------------------------------------------------
def count_all_values(nums):
    frequency = {}

    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    return frequency


# ------------------------------------------------------------
# Solution 4: Count characters in a string
# Time: O(n)
# ------------------------------------------------------------
def count_characters(text):
    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


# ------------------------------------------------------------
# Run examples
# ------------------------------------------------------------
nums = [1, 2, 3, 2, 4, 2, 5]

print("List:", nums)

target = 2
print("\nCount using loop:", count_value_loop(nums, target))
print("Count using builtin:", count_value_builtin(nums, target))

print("\nFrequency of all values:")
print(count_all_values(nums))

text = "banana"
print("\nCharacter count in:", text)
print(count_characters(text))