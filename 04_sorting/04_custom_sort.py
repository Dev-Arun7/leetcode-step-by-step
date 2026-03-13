"""
custom_sort.py

What you will learn:
- What custom sorting means
- How to use the key= parameter
- How to sort numbers using custom rules
- How to sort objects or lists using specific fields

Idea:

Normally Python sorts values directly.

Example:
sorted([5,2,8,1])

But sometimes we want to sort using a **rule**.

Examples:
- sort numbers by absolute value
- sort words by length
- sort intervals by start value
- sort students by score

For that we use:

key=
"""


# ------------------------------------------------------------
# Example 1: Sort numbers by absolute value
# ------------------------------------------------------------
# Absolute value ignores the sign of the number.

nums = [-10, 5, -3, 2, -1]

print("Original:", nums)

sorted_nums = sorted(nums, key=abs)

print("Sorted by absolute value:", sorted_nums)


# ------------------------------------------------------------
# Example 2: Sort words by length
# ------------------------------------------------------------
# Instead of alphabetical order,
# we sort based on word length.

words = ["apple", "fig", "banana", "kiwi"]

print("\nOriginal words:", words)

sorted_words = sorted(words, key=len)

print("Sorted by length:", sorted_words)


# ------------------------------------------------------------
# Example 3: Sort intervals by start value
# ------------------------------------------------------------

intervals = [[5,7], [1,3], [2,4]]

print("\nOriginal intervals:", intervals)

sorted_intervals = sorted(intervals, key=lambda x: x[0])

print("Sorted by start value:", sorted_intervals)


# ------------------------------------------------------------
# Example 4: Sort intervals by end value
# ------------------------------------------------------------

sorted_by_end = sorted(intervals, key=lambda x: x[1])

print("Sorted by end value:", sorted_by_end)


# ------------------------------------------------------------
# Example 5: Sort by multiple conditions
# ------------------------------------------------------------
# First sort by length
# Then alphabetically if lengths match

words2 = ["bat", "apple", "car", "banana", "ant", "dog"]

print("\nOriginal words:", words2)

sorted_words2 = sorted(words2, key=lambda w: (len(w), w))

print("Sorted by length then alphabetically:", sorted_words2)


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# key= tells Python:
#
# "Use this rule when comparing elements"
#
# Example:
#
# key=len
# → compare based on length
#
# key=abs
# → compare based on absolute value
#
# key=lambda x: x[0]
# → compare based on first value


# ------------------------------------------------------------
# Beginner mistakes
# ------------------------------------------------------------
# 1. Forgetting lambda
#
# Wrong:
# key=x[0]
#
# Correct:
# key=lambda x: x[0]
#
#
# 2. Confusing key with comparison
#
# key= does NOT change the element
# it only decides how sorting compares elements
#
#
# 3. Using sorted(list) when you want to modify the list
#
# sorted(list) returns a new list
#
# list.sort() changes the original list


# ------------------------------------------------------------
# Runnable examples
# ------------------------------------------------------------
nums2 = [3, -7, 1, -4, 9]

print("\nOriginal numbers:", nums2)
print("Sorted by absolute value:", sorted(nums2, key=abs))


students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Charlie", 78],
    ["David", 92]
]

print("\nStudents:", students)

# Sort by score
print("Sorted by score:", sorted(students, key=lambda s: s[1]))

# Sort by score then name
print("Sorted by score then name:", sorted(students, key=lambda s: (s[1], s[0])))


# ------------------------------------------------------------
# Small Practice
# ------------------------------------------------------------
# 1. Sort numbers by their last digit
#
# Example:
# [23, 45, 12, 19]
#
# Last digits:
# 3,5,2,9
#
# Result should be sorted based on those digits
#
#
# 2. Sort words by their last character
#
# Example:
# ["cat", "apple", "dog"]
#
#
# 3. Sort intervals by length
#
# Example:
# [start, end]
#
# length = end - start
#
#
# 4. Sort students by highest score first
#
#
# 5. Try sorting:
#
# nums = [-8, -3, 2, 7, -1]
#
# by:
# - absolute value
# - descending order