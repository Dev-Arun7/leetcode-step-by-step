"""
DIGIT EXTRACTION BASICS
=======================

The purpose is to learn how to:
- Extract digits from an integer
- Store digits in a list
- Extract digits from right to left
- Extract digits from left to right
- Reverse extracted digits
- Process each digit while looping
- Understand useful digit patterns for LeetCode problems

These techniques are useful when a problem asks you to work
with the individual digits of a number.

Example:

    num = 12345

    Digits:
    [1, 2, 3, 4, 5]

    Reversed:
    [5, 4, 3, 2, 1]


IMPORTANT:
When using %, // and integer division, digits are naturally
extracted from RIGHT to LEFT.

Example:

    12345

    12345 % 10 -> 5
    1234  % 10 -> 4
    123   % 10 -> 3
    12    % 10 -> 2
    1     % 10 -> 1
"""


# ------------------------------------------------------------
# Example number
# ------------------------------------------------------------
num = 12345


# ------------------------------------------------------------
# 1. Extract digits from RIGHT to LEFT
# ------------------------------------------------------------
# This is the most common method when working with digits.
#
# % 10 gives the last digit.
# // 10 removes the last digit.
#
# Example:
#
# 12345 % 10 -> 5
# 12345 // 10 -> 1234
#
# 1234 % 10 -> 4
# 1234 // 10 -> 123
#
# Result:
# [5, 4, 3, 2, 1]
# ------------------------------------------------------------

digits = []
temp = num

while temp > 0:
    digit = temp % 10
    digits.append(digit)

    temp = temp // 10

print("Original number:", num)
print("Digits (right to left):", digits)


# ------------------------------------------------------------
# 2. Reverse the extracted list
# ------------------------------------------------------------
# The list above is naturally created in reverse order.
#
# [5, 4, 3, 2, 1]
#
# Reverse it to get:
#
# [1, 2, 3, 4, 5]
# ------------------------------------------------------------

digits.reverse()

print("Digits reversed:", digits)


# ------------------------------------------------------------
# 3. Extract digits from LEFT to RIGHT
# ------------------------------------------------------------
# If we want the digits in their original order:
#
# 12345 -> [1, 2, 3, 4, 5]
#
# One simple method is:
#
# 1. Extract from right to left
# 2. Reverse the list
# ------------------------------------------------------------

digits = []
temp = num

while temp > 0:
    digit = temp % 10
    digits.append(digit)

    temp = temp // 10

digits.reverse()

print("Digits (left to right):", digits)


# ------------------------------------------------------------
# 4. Extract digits from LEFT to RIGHT using a string
# ------------------------------------------------------------
# Another easy method is to convert the number into a string.
#
# 12345 -> "12345"
#
# Then loop through each character.
#
# int("1") -> 1
# int("2") -> 2
# ...
#
# This is very easy to understand, but it uses string conversion.
# ------------------------------------------------------------

digits = []

for x in str(num):
    digits.append(int(x))

print("Digits using string:", digits)


# ------------------------------------------------------------
# 5. Shorter version using list comprehension
# ------------------------------------------------------------
# Same idea as above, but written in one line.
#
# This is useful to know, but the normal for loop is easier
# for beginners to understand.
# ------------------------------------------------------------

digits = [int(x) for x in str(num)]

print("Digits using list comprehension:", digits)


# ------------------------------------------------------------
# 6. Process each digit from LEFT to RIGHT
# ------------------------------------------------------------
# Once the digits are inside a list, we can process them
# just like any normal list.
#
# Example:
#
# [1, 2, 3, 4, 5]
#
# We can calculate the sum, find a maximum, count values, etc.
# ------------------------------------------------------------

digits = [int(x) for x in str(num)]

total = 0

for digit in digits:
    total = total + digit

print("Digits:", digits)
print("Sum of digits:", total)


# ------------------------------------------------------------
# 7. Process each digit from RIGHT to LEFT
# ------------------------------------------------------------
# We can also process the number directly without creating
# a list first.
#
# Example:
#
# 12345
#
# First -> 5
# Then  -> 4
# Then  -> 3
# Then  -> 2
# Then  -> 1
# ------------------------------------------------------------

temp = num

while temp > 0:
    digit = temp % 10

    print("Current digit:", digit)

    temp = temp // 10


# ------------------------------------------------------------
# 8. Store digits from RIGHT to LEFT
# ------------------------------------------------------------
# This is useful when the problem naturally works with the
# last digit first.
#
# Example:
#
# 12345 -> [5, 4, 3, 2, 1]
# ------------------------------------------------------------

digits = []
temp = num

while temp > 0:
    digits.append(temp % 10)
    temp = temp // 10

print("Right-to-left digits:", digits)


# ------------------------------------------------------------
# 9. Store digits from LEFT to RIGHT
# ------------------------------------------------------------
# Extracting with % 10 gives right-to-left order.
#
# So we reverse the list afterwards.
#
# Example:
#
# First:
# [5, 4, 3, 2, 1]
#
# After reverse:
# [1, 2, 3, 4, 5]
# ------------------------------------------------------------

digits = []
temp = num

while temp > 0:
    digits.append(temp % 10)
    temp = temp // 10

digits.reverse()

print("Left-to-right digits:", digits)


# ------------------------------------------------------------
# 10. Reverse a number without using a list
# ------------------------------------------------------------
# Sometimes we don't need the individual digits in a list.
#
# We can directly build the reversed number.
#
# Example:
#
# 12345
#
# digit = 5
# reverse = 5
#
# digit = 4
# reverse = 54
#
# digit = 3
# reverse = 543
#
# Result:
# 54321
# ------------------------------------------------------------

temp = num
reverse = 0

while temp > 0:
    digit = temp % 10

    reverse = reverse * 10 + digit

    temp = temp // 10

print("Original number:", num)
print("Reversed number:", reverse)


# ------------------------------------------------------------
# QUICK REFERENCE
# ------------------------------------------------------------
#
# num % 10
#     -> Get the LAST digit
#
# num // 10
#     -> REMOVE the LAST digit
#
# list.append(digit)
#     -> Add a digit to a list
#
# list.reverse()
#     -> Reverse the list
#
# str(num)
#     -> Convert number to string
#
# int("5")
#     -> Convert a character back to an integer
#
#
# Example:
#
# num = 12345
#
# RIGHT -> LEFT:
#
# 12345 % 10 -> 5
# 1234  % 10 -> 4
# 123   % 10 -> 3
# 12    % 10 -> 2
# 1     % 10 -> 1
#
# Result:
# [5, 4, 3, 2, 1]
#
#
# LEFT -> RIGHT:
#
# Extract first:
# [5, 4, 3, 2, 1]
#
# Then reverse:
# [1, 2, 3, 4, 5]
#
#
# STRING METHOD:
#
# str(12345)
# -> "12345"
#
# Loop:
# "1" -> 1
# "2" -> 2
# "3" -> 3
# "4" -> 4
# "5" -> 5
#
# Result:
# [1, 2, 3, 4, 5]
#
#
# ------------------------------------------------------------
# WHEN THIS IS USEFUL IN LEETCODE
# ------------------------------------------------------------
#
# These basic patterns become useful when a problem asks you to:
#
# - Work with individual digits
# - Reverse a number
# - Check digits one by one
# - Count specific digits
# - Find the sum of digits
# - Find the largest/smallest digit
# - Compare digits
# - Build a new number from digits
# - Store digits and process them like a list
#
# The important thing is not to memorize a complete solution.
#
# Remember these basic tools:
#
#     % 10   -> get last digit
#     // 10  -> remove last digit
#     append -> store digit
#     reverse -> change the order
#     str()  -> process digits from left to right easily
#
# These small building blocks can be combined later to solve
# many different LeetCode problems.
# ------------------------------------------------------------