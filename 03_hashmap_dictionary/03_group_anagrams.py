"""
group_anagrams.py

What you will learn:
- What an anagram is
- How to group words using a hashmap
- How to build a key for words that belong together
- Why dictionaries are great for "grouping" problems

Real idea:
Imagine words are going to a party.

Words that are anagrams of each other belong to the same friend group.

For example:
"eat", "tea", and "ate" all use the same letters,
so they should stand together in the same group.

Goal:
Given a list of strings, group the anagrams together.

Example:
Input:
["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]

Important:
The order of groups may be different.
The order inside each group may also be different.
That is okay.
"""


# ------------------------------------------------------------
# Warm-up: What is an anagram?
# ------------------------------------------------------------
# Two words are anagrams if they use the same letters
# with the same counts.
#
# Examples:
# "eat" and "tea" -> yes
# "listen" and "silent" -> yes
# "rat" and "car" -> no
#
# One simple trick:
# If two words become the same after sorting,
# they are anagrams.
#
# "eat" -> "aet"
# "tea" -> "aet"
# "ate" -> "aet"
#
# Same sorted form = same group


# ------------------------------------------------------------
# Solution 1: Group using sorted word as key
# ------------------------------------------------------------
# Idea:
# 1. For each word, sort its letters
# 2. Use that sorted result as a dictionary key
# 3. Add the original word into that group
#
# Example:
# "eat" -> key = "aet"
# "tea" -> key = "aet"
# "bat" -> key = "abt"
#
# Dictionary:
# {
#     "aet": ["eat", "tea", "ate"],
#     "ant": ["tan", "nat"],
#     "abt": ["bat"]
# }
#
# Time:
# Sorting each word takes O(k log k)
# Total is about O(n * k log k)
#
# n = number of words
# k = average word length

def group_anagrams(words):
    groups = {}

    for word in words:
        sorted_word = sorted(word)          # Example: "eat" -> ['a', 'e', 't']
        key = "".join(sorted_word)          # Turn list into string: "aet"

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


# ------------------------------------------------------------
# Solution 2: Same idea, written a little shorter
# ------------------------------------------------------------
# This version is still beginner friendly,
# but Solution 1 is easier to understand first.

def group_anagrams_clean(words):
    groups = {}

    for word in words:
        key = "".join(sorted(word))

        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    return list(groups.values())


# ------------------------------------------------------------
# Step-by-step dry run
# ------------------------------------------------------------
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
#
# Start:
# groups = {}
#
# word = "eat"
# key = "aet"
# groups = {
#     "aet": ["eat"]
# }
#
# word = "tea"
# key = "aet"
# groups = {
#     "aet": ["eat", "tea"]
# }
#
# word = "tan"
# key = "ant"
# groups = {
#     "aet": ["eat", "tea"],
#     "ant": ["tan"]
# }
#
# word = "ate"
# key = "aet"
# groups = {
#     "aet": ["eat", "tea", "ate"],
#     "ant": ["tan"]
# }
#
# word = "nat"
# key = "ant"
# groups = {
#     "aet": ["eat", "tea", "ate"],
#     "ant": ["tan", "nat"]
# }
#
# word = "bat"
# key = "abt"
# groups = {
#     "aet": ["eat", "tea", "ate"],
#     "ant": ["tan", "nat"],
#     "abt": ["bat"]
# }
#
# Final answer:
# list(groups.values())


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# The biggest idea in this problem is:
#
# We are not using the original word as the key.
# We are using a "normalized form" of the word.
#
# In this case:
# normalized form = sorted letters
#
# That means different words can point to the same key.
#
# "eat" -> "aet"
# "tea" -> "aet"
# "ate" -> "aet"
#
# This is a very important hashmap pattern:
#
# "Convert something into a form that makes matching easy."
#
# You will use this idea again in harder problems too.


# ------------------------------------------------------------
# Beginner mistakes
# ------------------------------------------------------------
# 1. Trying to use sorted(word) directly as a dictionary key
#
#    sorted(word) gives a list, like ['a', 'e', 't']
#    Lists cannot be dictionary keys because they are mutable.
#
#    So we convert it into a string:
#    "".join(sorted(word))
#
#
# 2. Storing the sorted word instead of the original word
#
#    Wrong:
#    groups[key].append(key)
#
#    We want to group the ORIGINAL words.
#
#
# 3. Forgetting to create the list first
#
#    Before appending, make sure the key exists.
#
#
# 4. Returning the dictionary instead of the grouped lists
#
#    Usually the problem wants:
#    list(groups.values())
#
#
# 5. Thinking same length means anagram
#
#    "cat" and "dog" have same length
#    but they are not anagrams.


# ------------------------------------------------------------
# Fun mini helper: show groups nicely
# ------------------------------------------------------------
def print_groups(title, groups):
    print("\n" + title)
    for group in groups:
        print(group)


# ------------------------------------------------------------
# Runnable examples
# ------------------------------------------------------------
words1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
result1 = group_anagrams(words1)

print("Example 1")
print("Input:", words1)
print_groups("Grouped anagrams:", result1)


words2 = [""]
result2 = group_anagrams(words2)

print("\nExample 2")
print("Input:", words2)
print_groups("Grouped anagrams:", result2)


words3 = ["a"]
result3 = group_anagrams(words3)

print("\nExample 3")
print("Input:", words3)
print_groups("Grouped anagrams:", result3)


words4 = ["rat", "tar", "art", "car"]
result4 = group_anagrams(words4)

print("\nExample 4")
print("Input:", words4)
print_groups("Grouped anagrams:", result4)


words5 = ["listen", "silent", "evil", "vile", "veil", "stone"]
result5 = group_anagrams(words5)

print("\nExample 5")
print("Input:", words5)
print_groups("Grouped anagrams:", result5)


# ------------------------------------------------------------
# Small practice tasks
# ------------------------------------------------------------
# Try these on your own:
#
# 1. Count how many anagram groups are formed
#
#    Example:
#    ["eat", "tea", "bat"] -> 2 groups
#
#
# 2. Return only groups that contain more than 1 word
#
#    Example:
#    ["eat", "tea", "bat"] -> [["eat", "tea"]]
#
#
# 3. Find the largest anagram group
#
#    Example:
#    ["eat", "tea", "ate", "bat"] -> ["eat", "tea", "ate"]
#
#
# 4. Make the output groups sorted alphabetically
#
#    Example:
#    ["tea", "eat", "ate"] -> ["ate", "eat", "tea"]
#
#
# 5. Bonus thought:
#    Can you solve this without sorting each word?
#    Hint:
#    What if you count letters instead?


# ------------------------------------------------------------
# Tiny recap
# ------------------------------------------------------------
# If a problem says:
# - group similar items
# - detect matching patterns
# - collect things that "belong together"
#
# Ask yourself:
# "Can I build a key and use a hashmap?"
#
# That is the main pattern here.