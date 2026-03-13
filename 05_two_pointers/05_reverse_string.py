"""
What you will learn:
- How to use two pointers from both ends
- How to reverse a string step by step
- How swapping works

Problem:

Given a string, return it in reverse order.

Example:
"hello" -> "olleh"

Important:
Strings in Python cannot be changed in place.

So one common way is:
1. convert string to a list
2. swap characters using two pointers
3. join back into a string
"""


# ------------------------------------------------------------
# Simple Python Shortcut
# ------------------------------------------------------------
# Python has a quick way:
#
# s[::-1]
#
# But in this file, we want to LEARN
# how reversing works using two pointers.

def reverse_string_shortcut(s):
    return s[::-1]


# ------------------------------------------------------------
# Two Pointer Approach
# ------------------------------------------------------------
# Idea:
#
# left starts at the beginning
# right starts at the end
#
# Swap both characters
# Move left forward
# Move right backward
#
# Continue until they cross

def reverse_string(s):

    chars = list(s)

    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]

        left += 1
        right -= 1

    return "".join(chars)


# ------------------------------------------------------------
# Step-by-step example
# ------------------------------------------------------------
# s = "hello"
#
# chars = ['h', 'e', 'l', 'l', 'o']
#
# left = 0, right = 4
# swap h and o
# ['o', 'e', 'l', 'l', 'h']
#
# left = 1, right = 3
# swap e and l
# ['o', 'l', 'l', 'e', 'h']
#
# left = 2, right = 2
# stop
#
# answer = "olleh"


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# This is one of the easiest two pointer patterns:
#
# start from both ends
# swap
# move inward
#
# This same idea is also used in:
# - palindrome checking
# - reversing arrays
# - some string problems


# ------------------------------------------------------------
# Beginner Mistakes
# ------------------------------------------------------------
# 1. Trying to change a string directly
#
# Strings are immutable in Python.
#
# Wrong:
# s[0] = 'x'
#
# 2. Forgetting to convert to list first
#
# list(s)
#
# 3. Forgetting to join the list back into a string
#
# "".join(chars)
#
# 4. Using while left <= right
#
# while left < right is enough
#
# 5. Mixing up index and character
#
# left and right are positions
# chars[left] and chars[right] are characters


# ------------------------------------------------------------
# Helper function with steps
# ------------------------------------------------------------
def reverse_string_with_steps(s):

    chars = list(s)

    left = 0
    right = len(chars) - 1

    print("\nOriginal:", s)

    while left < right:
        print("Before swap:", chars)
        print("Swap", chars[left], "and", chars[right])

        chars[left], chars[right] = chars[right], chars[left]

        print("After swap: ", chars)

        left += 1
        right -= 1

    result = "".join(chars)
    print("Reversed:", result)

    return result


# ------------------------------------------------------------
# Runnable examples
# ------------------------------------------------------------
print("Shortcut:", reverse_string_shortcut("hello"))
print("Two pointers:", reverse_string("hello"))

print("\nTwo pointers:", reverse_string("python"))
print("Two pointers:", reverse_string("a"))
print("Two pointers:", reverse_string(""))
print("Two pointers:", reverse_string("racecar"))

reverse_string_with_steps("hello")


# ------------------------------------------------------------
# Small Practice
# ------------------------------------------------------------
# 1. Reverse a list of numbers using two pointers
#
# Example:
# [1, 2, 3, 4] -> [4, 3, 2, 1]
#
#
# 2. Check if a string is a palindrome
#
# Example:
# "madam" -> True
# "hello" -> False
#
#
# 3. Reverse only the vowels in a string
#
# Example:
# "hello" -> "holle"
#
#
# 4. Try writing the same logic without using
# Python slicing
#
#
# 5. Dry run this by hand:
# "abcd"