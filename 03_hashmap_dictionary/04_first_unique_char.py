"""
first_unique_char.py

What you will learn:
- How to count characters using a hashmap
- How to solve a problem in two passes
- How to find the first character that appears only once
- Why counting first makes checking easier later

Fun idea:
Imagine each character is standing in a line.

Some characters have twins.
Some characters appear many times.
But one character is standing all alone.

Your job:
Find the first lonely character.

Problem:
Given a string s, return the index of the first non-repeating character.

If every character repeats, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
"""


# ------------------------------------------------------------
# Why this problem is important
# ------------------------------------------------------------
# This problem teaches a very common hashmap pattern:
#
# Step 1: Count frequency
# Step 2: Use those counts to answer the question
#
# Instead of storing characters, we store how many
# times each character appears.


# ------------------------------------------------------------
# Solution 1: Count first, then check
# ------------------------------------------------------------
# Pass 1:
# Count how many times each character appears
#
# Pass 2:
# Walk through the string again
# Return the first index whose character count is 1
#
# Time: O(n)
# Space: O(n)

def first_unique_char(s):
    counts = {}

    # First pass: count characters
    for ch in s:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

    # Second pass: find first unique character
    for i in range(len(s)):
        ch = s[i]
        if counts[ch] == 1:
            return i

    return -1


# ------------------------------------------------------------
# Solution 2: Same idea using enumerate
# ------------------------------------------------------------

def first_unique_char_clean(s):
    counts = {}

    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i

    return -1


# ------------------------------------------------------------
# Step-by-step dry run
# ------------------------------------------------------------
# s = "loveleetcode"
#
# counts:
# l -> 2
# o -> 2
# v -> 1
# e -> 4
# t -> 1
# c -> 1
# d -> 1
#
# Now scan again:
# l -> no
# o -> no
# v -> yes -> return index 2


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# This problem teaches a common pattern:
#
# 1. Collect information first
# 2. Use that information later
#
# Here:
# - collect = count characters
# - use = find first count == 1


# ------------------------------------------------------------
# Beginner mistakes
# ------------------------------------------------------------
# 1. Looping over the dictionary in the second pass
#
#    That does not preserve the original string order.
#    We must scan the string again.
#
# 2. Confusing character and index
#
#    i = index
#    s[i] = character


# ------------------------------------------------------------
# Helper function for display
# ------------------------------------------------------------
def show_result(s):
    index = first_unique_char(s)

    print("\nString:", s)
    print("First unique character index:", index)

    if index != -1:
        print("Character:", s[index])
    else:
        print("No unique character found.")


# ------------------------------------------------------------
# Runnable examples
# ------------------------------------------------------------
show_result("leetcode")
show_result("loveleetcode")
show_result("aabb")
show_result("abcabcde")
show_result("")
show_result("z")
show_result("aabbccd")


# ------------------------------------------------------------
# Small practice
# ------------------------------------------------------------
# 1. Return the first unique character itself
#    instead of its index.
#
# 2. Count how many unique characters exist.
#
# 3. Return all characters that appear only once.