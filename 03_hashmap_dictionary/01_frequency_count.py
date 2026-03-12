"""
What you learn:
- How to count frequency using a dictionary
- Why hashmap/dictionary is useful
- How to build frequency maps step by step
- How this is different from simple counting

Where this is used:
Frequency counting is one of the most important patterns in LeetCode.

Examples:
- Count numbers in an array
- Count characters in a string
- Find duplicates
- Find most frequent element
- Anagram problems

What is frequency count?
It means:
Count how many times each value appears.

Example:
[1, 2, 2, 3, 1, 1]

Frequency:
1 -> 3
2 -> 2
3 -> 1
"""


# ------------------------------------------------------------
# Solution 1: Frequency count using normal dictionary logic
# ------------------------------------------------------------
# If value already exists, increase count
# Otherwise start with 1

def frequency_count(nums):

    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq


# ------------------------------------------------------------
# Solution 2: Frequency count using dict.get()
# ------------------------------------------------------------
# dict.get(key, default_value)
# If key is missing, return default value

def frequency_count_get(nums):

    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    return freq


# ------------------------------------------------------------
# Solution 3: Character frequency in string
# ------------------------------------------------------------
# Same idea, but for characters instead of numbers

def character_frequency(text):

    freq = {}

    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# This pattern is very important:
#
# freq[num] = freq.get(num, 0) + 1
#
# Meaning:
# - If num already exists, get its current count
# - If num does not exist, start from 0
# - Then add 1
#
# This idea appears in many problems:
# - Counting numbers
# - Counting characters
# - Duplicates
# - Anagrams
# - Most frequent element
#
# When you see:
# "count how many times"
# think:
# "use a hashmap / dictionary"


# ------------------------------------------------------------
# Common Beginner Mistakes
# ------------------------------------------------------------
# 1. Doing freq[num] += 1 before the key exists
#    This gives an error
#
# 2. Forgetting that dictionary stores:
#    key -> value
#
# 3. Confusing a single counter with frequency counting
#
#    count = count + 1   -> counts one thing
#    freq[num] += 1      -> counts each value separately


# ------------------------------------------------------------
# Run examples
# ------------------------------------------------------------
nums = [1, 2, 2, 3, 1, 1, 4]

print("List:", nums)

print("\nSolution 1 (normal dictionary logic):")
print(frequency_count(nums))

print("\nSolution 2 (using get):")
print(frequency_count_get(nums))


text = "banana"

print("\nString:", text)
print("Character frequency:")
print(character_frequency(text))


# Edge cases
nums2 = []
print("\nEmpty list:")
print(frequency_count(nums2))

text2 = ""
print("\nEmpty string:")
print(character_frequency(text2))


# ------------------------------------------------------------
# Small Practice
# ------------------------------------------------------------
# Try modifying this code to solve these:
#
# 1. Find the most frequent number in a list
#
# 2. Find all values that appear more than once
#
# 3. Count words in a sentence
#
# Example:
# "i love python and i love coding"
#
# 4. Count uppercase and lowercase letters separately