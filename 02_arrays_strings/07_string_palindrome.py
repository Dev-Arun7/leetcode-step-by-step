"""
What you learn:
- How to check if a string is a palindrome
- Multiple ways to solve the same problem
- Reversing and comparing
- Comparing characters from both ends
- Introduction to the two-pointer technique

Where this is used:
Palindrome problems are very common in coding interviews.

Examples:
- Valid palindrome
- Longest palindrome
- Reverse and compare problems
- Two pointer problems

What is a palindrome?
A palindrome reads the same from left to right and right to left.

Examples:
"malayalam"-> palindrome
"racecar" -> palindrome
"hello" -> not palindrome
"""


# ------------------------------------------------------------
# Solution 1: Reverse and compare using slicing
# ------------------------------------------------------------
# Reverse the string and compare with original string

def is_palindrome_slice(text):

    return text == text[::-1]


# ------------------------------------------------------------
# Solution 2: Two pointers
# ------------------------------------------------------------
# Compare first and last characters,
# then move toward the center.

def is_palindrome_two_pointers(text):

    left = 0
    right = len(text) - 1

    while left < right:

        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True


# ------------------------------------------------------------
# Solution 3: Build reversed string using loop
# ------------------------------------------------------------
# This is good for learning how reversing works.

def is_palindrome_loop(text):

    reversed_text = ""

    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]

    return text == reversed_text


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# The two-pointer idea is very important.
#
# Example:
#
# text = "madam"
#
# left  -> m
# right -> m
#
# Then move inward:
#
# left  -> a
# right -> a
#
# Then move inward again:
#
# left  -> d
# right -> d
#
# If all matching characters are equal,
# the string is a palindrome.
#
# This idea appears in many problems:
# - Palindrome check
# - Reverse string
# - Pair problems in sorted arrays
# - Container with most water


# ------------------------------------------------------------
# Common Beginner Mistakes
# ------------------------------------------------------------
# 1. Forgetting to move both pointers
#
# 2. Using left <= right instead of left < right
#    It may still work, but left < right is cleaner
#
# 3. Comparing wrong characters
#
# 4. Building reversed string for very large input
#    Two pointers can be more efficient


# ------------------------------------------------------------
# Run examples
# ------------------------------------------------------------
text1 = "malayalam"
print("Text:", text1)
print("Solution 1 (slice):", is_palindrome_slice(text1))
print("Solution 2 (two pointers):", is_palindrome_two_pointers(text1))
print("Solution 3 (loop):", is_palindrome_loop(text1))

text2 = "racecar"
print("\nText:", text2)
print("Solution 1 (slice):", is_palindrome_slice(text2))
print("Solution 2 (two pointers):", is_palindrome_two_pointers(text2))
print("Solution 3 (loop):", is_palindrome_loop(text2))

text3 = "hello"
print("\nText:", text3)
print("Solution 1 (slice):", is_palindrome_slice(text3))
print("Solution 2 (two pointers):", is_palindrome_two_pointers(text3))
print("Solution 3 (loop):", is_palindrome_loop(text3))

text4 = ""
print("\nText:", text4)
print("Solution 1 (slice):", is_palindrome_slice(text4))
print("Solution 2 (two pointers):", is_palindrome_two_pointers(text4))
print("Solution 3 (loop):", is_palindrome_loop(text4))


# ------------------------------------------------------------
# Small Practice
# ------------------------------------------------------------
# Try modifying this code to solve these:
#
# 1. Ignore uppercase/lowercase
#    Example: "Madam" should be palindrome
#
# 2. Ignore spaces
#    Example: "nurses run" should be palindrome
#
# 3. Ignore spaces and special characters
#    Example: "A man, a plan, a canal: Panama"
#
# These are very common interview follow-up questions.