"""
sort_strings.py

What you will learn:
- How string sorting works in Python
- How words are sorted alphabetically
- How uppercase and lowercase affect sorting
- How to sort by length
- How to use custom sorting rules with key=

Important:
Python can sort strings directly.

But sometimes the default order is not what we want.
That is why learning custom sorting is useful.
"""


# ------------------------------------------------------------
# Basic string sorting
# ------------------------------------------------------------
# Python sorts strings in alphabetical order by default.

words = ["banana", "apple", "cherry", "mango"]

print("Original words:", words)
print("Sorted words:", sorted(words))


# ------------------------------------------------------------
# How sorting compares strings
# ------------------------------------------------------------
# Python compares strings character by character.
#
# Example:
# "apple" comes before "banana"
# because 'a' comes before 'b'

words2 = ["dog", "cat", "bat", "ant"]

print("\nOriginal words:", words2)
print("Sorted words:", sorted(words2))


# ------------------------------------------------------------
# Uppercase and lowercase
# ------------------------------------------------------------
# By default, uppercase letters and lowercase letters
# are treated differently.
#
# Usually uppercase letters come before lowercase letters.

words3 = ["apple", "Banana", "cherry", "Apple"]

print("\nOriginal words:", words3)
print("Default sorting:", sorted(words3))


# ------------------------------------------------------------
# Case-insensitive sorting
# ------------------------------------------------------------
# If we want sorting that ignores uppercase/lowercase,
# we can use key=str.lower

print("Case-insensitive sorting:", sorted(words3, key=str.lower))


# ------------------------------------------------------------
# Sorting by length
# ------------------------------------------------------------
# Sometimes we do not want alphabetical order.
# Sometimes we want shorter strings first.

words4 = ["pear", "watermelon", "kiwi", "fig", "banana"]

print("\nOriginal words:", words4)
print("Sorted by length:", sorted(words4, key=len))


# ------------------------------------------------------------
# Sorting by length, then alphabetically
# ------------------------------------------------------------
# We can use a tuple as the key.
#
# (length, word)
#
# That means:
# 1. sort by length
# 2. if lengths are same, sort alphabetically

words5 = ["bat", "apple", "car", "banana", "ant", "dog"]

print("\nOriginal words:", words5)
print("Sorted by length, then alphabetically:", sorted(words5, key=lambda word: (len(word), word)))


# ------------------------------------------------------------
# Reverse sorting
# ------------------------------------------------------------
# We can also sort in descending order.

words6 = ["banana", "apple", "cherry", "mango"]

print("\nOriginal words:", words6)
print("Reverse alphabetical order:", sorted(words6, reverse=True))


# ------------------------------------------------------------
# Sorting characters inside one string
# ------------------------------------------------------------
# Sometimes problems ask us to sort the letters of a word.
#
# Example:
# "eat" -> "aet"

word = "eat"
sorted_characters = sorted(word)
sorted_word = "".join(sorted_characters)

print("\nOriginal word:", word)
print("Sorted characters list:", sorted_characters)
print("Sorted word:", sorted_word)


# ------------------------------------------------------------
# Why this matters
# ------------------------------------------------------------
# Sorting characters in a word is useful in problems like:
# - anagrams
# - checking if two words use the same letters
# - grouping similar strings


# ------------------------------------------------------------
# Function: sort words alphabetically
# ------------------------------------------------------------
def sort_alphabetically(words):
    return sorted(words)


# ------------------------------------------------------------
# Function: sort words ignoring case
# ------------------------------------------------------------
def sort_ignore_case(words):
    return sorted(words, key=str.lower)


# ------------------------------------------------------------
# Function: sort by length
# ------------------------------------------------------------
def sort_by_length(words):
    return sorted(words, key=len)


# ------------------------------------------------------------
# Function: sort by length, then alphabetically
# ------------------------------------------------------------
def sort_by_length_then_alpha(words):
    return sorted(words, key=lambda word: (len(word), word))


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# The key= argument is very important.
#
# It tells Python:
# "Sort using this rule"
#
# Examples:
# key=len
# -> sort by length
#
# key=str.lower
# -> sort ignoring uppercase/lowercase
#
# key=lambda word: (len(word), word)
# -> sort by length first, then alphabetically
#
# This idea is used in many interview problems.


# ------------------------------------------------------------
# Beginner Mistakes
# ------------------------------------------------------------
# 1. Forgetting that sorted() returns a new list
#
#    sorted(words) does not change the original list
#
# 2. Forgetting that list.sort() changes the original list
#
# 3. Being surprised by uppercase/lowercase order
#
#    Default string sorting is case-sensitive
#
# 4. Using "".join(sorted(words))
#
#    That is wrong if words is a list of words
#
#    "".join(sorted(word)) works for one string
#    sorted(words) works for a list of strings
#
# 5. Mixing up:
#    sorted(word)   -> sorts characters of one word
#    sorted(words)  -> sorts a list of words


# ------------------------------------------------------------
# Runnable examples
# ------------------------------------------------------------
example_words = ["zebra", "apple", "Mango", "banana", "kiwi"]

print("\nExample list:", example_words)
print("Alphabetical:", sort_alphabetically(example_words))
print("Ignore case:", sort_ignore_case(example_words))
print("By length:", sort_by_length(example_words))
print("By length then alphabetically:", sort_by_length_then_alpha(example_words))


# ------------------------------------------------------------
# Small Practice (Explained)
# ------------------------------------------------------------

# 1. Sort words in reverse alphabetical order
#
# Input example:
# ["cat", "apple", "dog"]
#
# Reverse alphabetical order should give:
# ["dog", "cat", "apple"]
#
# Hint:
# sorted(words, reverse=True)



# 2. Sort words by their LAST character
#
# Input:
# ["cat", "apple", "dog"]
#
# Last characters:
# cat   -> t
# apple -> e
# dog   -> g
#
# Now sort by these letters: e, g, t
#
# Expected order:
# ["apple", "dog", "cat"]
#
# Hint:
# Use key=lambda word: word[-1]



# 3. Sort names ignoring uppercase/lowercase
#
# Input:
# ["Sun", "moon", "star", "Apple", "bat"]
#
# Default sorting treats uppercase differently.
#
# Default result might be:
# ['Apple', 'Sun', 'bat', 'moon', 'star']
#
# But if we ignore case we want:
# ['Apple', 'bat', 'moon', 'star', 'Sun']
#
# Hint:
# key=str.lower



# 4. Sort the letters inside each word
#
# Input:
# "tea"
#
# Sorted characters:
# "aet"
#
# Another example:
# "banana" -> "aaabnn"
#
# Hint:
# sorted(word) returns characters
# "".join(...) converts list back to string



# 5. Compare different types of sorting
#
# Use this list:
#
# ["Sun", "moon", "star", "Apple", "bat"]
#
# Try three things:
#
# A) Default sorting
#
# sorted(words)
#
# B) Case-insensitive sorting
#
# sorted(words, key=str.lower)
#
# C) Sorting by length
#
# sorted(words, key=len)
#
# Observe how the results change.