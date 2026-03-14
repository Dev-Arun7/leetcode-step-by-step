"""
longest_substring.py

What you will learn:
- How variable-size sliding windows work
- How to expand and shrink a window
- How to track characters using a set
- How to find the longest substring without repeating characters

Problem:

Given a string s, find the length of the longest substring
without repeating characters.

A substring means a continuous part of the string.

Example 1:
s = "abcabcbb"

Substrings without repeating characters:
"abc" -> length 3
"bca" -> length 3
"cab" -> length 3

Answer: 3

Example 2:
s = "bbbbb"

Longest substring:
"b" -> length 1

Answer: 1

Example 3:
s = "pwwkew"

Longest substring:
"wke" -> length 3

Answer: 3
"""


# ------------------------------------------------------------
# Brute Force Approach
# ------------------------------------------------------------
# Check every possible substring.
# For each substring, check whether all characters are unique.
#
# Time: O(n^3) in the simple version
# Space: O(n)

def longest_substring_bruteforce(s):

    max_length = 0

    for start in range(len(s)):
        for end in range(start, len(s)):

            substring = s[start:end + 1]

            if has_all_unique_characters(substring):
                max_length = max(max_length, len(substring))

    return max_length


def has_all_unique_characters(text):

    seen = set()

    for ch in text:
        if ch in seen:
            return False
        seen.add(ch)

    return True


# ------------------------------------------------------------
# Sliding Window Approach
# ------------------------------------------------------------
# Idea:
#
# Use a window from left to right.
# Expand the window by moving right.
#
# If a character repeats,
# shrink the window from the left
# until the window becomes valid again.
#
# Keep track of the longest valid window.

def longest_substring(s):

    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        window_length = right - left + 1
        max_length = max(max_length, window_length)

    return max_length


# ------------------------------------------------------------
# Step-by-step example
# ------------------------------------------------------------
# s = "abcabcbb"
#
# right = 0 -> "a"
# window = "a" -> length 1
#
# right = 1 -> "ab"
# window = "ab" -> length 2
#
# right = 2 -> "abc"
# window = "abc" -> length 3
#
# right = 3 -> "a" repeats
#
# remove from left until "a" is gone
# then continue
#
# final answer = 3


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# This is a variable-size sliding window problem.
#
# The window grows when it is valid.
# The window shrinks when it becomes invalid.
#
# Valid means:
# no repeated characters inside the current window.
#
# This pattern is common in substring problems.


# ------------------------------------------------------------
# Beginner Mistakes
# ------------------------------------------------------------
# 1. Confusing substring with subsequence
#
# Substring must be continuous.
#
# 2. Clearing the whole set when a duplicate appears
#
# We only shrink the window as much as needed.
#
# 3. Forgetting the while loop
#
# A repeated character may require removing
# more than one character from the left.
#
# 4. Updating max_length before fixing the window
#
# First make the window valid, then update the answer.


# ------------------------------------------------------------
# Helper function to show one actual substring
# ------------------------------------------------------------
def longest_substring_value(s):

    seen = set()
    left = 0
    max_length = 0
    best_start = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        window_length = right - left + 1

        if window_length > max_length:
            max_length = window_length
            best_start = left

    return s[best_start:best_start + max_length]


# ------------------------------------------------------------
# Runnable Examples
# ------------------------------------------------------------
s1 = "abcabcbb"
print("String:", s1)
print("Brute force:", longest_substring_bruteforce(s1))
print("Sliding window:", longest_substring(s1))
print("One longest substring:", longest_substring_value(s1))


s2 = "bbbbb"
print("\nString:", s2)
print("Sliding window:", longest_substring(s2))
print("One longest substring:", longest_substring_value(s2))


s3 = "pwwkew"
print("\nString:", s3)
print("Sliding window:", longest_substring(s3))
print("One longest substring:", longest_substring_value(s3))


s4 = ""
print("\nString:", s4)
print("Sliding window:", longest_substring(s4))
print("One longest substring:", longest_substring_value(s4))


s5 = "dvdf"
print("\nString:", s5)
print("Sliding window:", longest_substring(s5))
print("One longest substring:", longest_substring_value(s5))


# ------------------------------------------------------------
# Small Practice
# ------------------------------------------------------------
# 1. Return the actual longest substring
#    instead of only its length
#
# Example:
# "abcabcbb" -> "abc"
#
#
# 2. Count how many substrings have all unique characters
#
#
# 3. Find the longest substring with at most 2 distinct characters
#
#
# 4. Try solving this problem with brute force first
#    and compare the time complexity
#
#
# 5. Dry run this input by hand:
#    "abba"