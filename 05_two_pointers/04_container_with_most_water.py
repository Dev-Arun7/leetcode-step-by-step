"""
container_with_most_water.py

What you will learn:
- How to use two pointers from both ends
- How to calculate area between two lines
- Why moving the shorter line is the correct idea

Problem:

You are given an array where each value represents the height of a vertical line.

Example:
height = [1,8,6,2,5,4,8,3,7]

Pick two lines that can hold the most water.

Water area formula:

width * min(left_height, right_height)

Example:
If left height = 8 and right height = 7
and distance between them = 7

area = 7 * min(8, 7)
area = 7 * 7
area = 49
"""


# ------------------------------------------------------------
# Brute Force Approach
# ------------------------------------------------------------
# Check every pair of lines.
#
# Time: O(n^2)
# Space: O(1)

def max_water_bruteforce(height):

    max_area = 0

    for i in range(len(height)):
        for j in range(i + 1, len(height)):

            width = j - i
            current_height = min(height[i], height[j])
            area = width * current_height

            if area > max_area:
                max_area = area

    return max_area


# ------------------------------------------------------------
# Two Pointer Approach
# ------------------------------------------------------------
# Start with the widest container:
# left at the beginning
# right at the end
#
# At each step:
# - calculate area
# - update max area
# - move the shorter line inward
#
# Why move the shorter line?
# Because the shorter line limits the height.
# Moving the taller line usually does not help.

def max_water(height):

    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:

        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height

        if area > max_area:
            max_area = area

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# ------------------------------------------------------------
# Step-by-step example
# ------------------------------------------------------------
# height = [1,8,6,2,5,4,8,3,7]
#
# left = 0, right = 8
#
# heights = 1 and 7
# width = 8
# area = 8 * min(1,7) = 8
#
# Move left because 1 is smaller
#
# left = 1, right = 8
# heights = 8 and 7
# width = 7
# area = 7 * min(8,7) = 49
#
# max_area = 49


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# Important idea:
#
# Area depends on:
# 1. width
# 2. shorter height
#
# Even if width becomes smaller,
# we may still get a bigger area
# if the shorter height becomes taller.
#
# That is why we move the shorter pointer.
#
# If we move the taller pointer,
# the shorter height stays the same,
# so the area cannot improve much.


# ------------------------------------------------------------
# Beginner Mistakes
# ------------------------------------------------------------
# 1. Using max(height[left], height[right])
#
# Wrong:
# area uses the shorter line, not the taller one
#
# Correct:
# min(height[left], height[right])
#
#
# 2. Moving both pointers together
#
# Only move one pointer at a time
#
#
# 3. Moving the taller pointer
#
# The shorter line is the limiting factor
#
#
# 4. Forgetting that width = right - left
#
# Width is distance between indices


# ------------------------------------------------------------
# Runnable Examples
# ------------------------------------------------------------
heights1 = [1,8,6,2,5,4,8,3,7]
print("Heights:", heights1)
print("Brute force:", max_water_bruteforce(heights1))
print("Two pointers:", max_water(heights1))


heights2 = [1,1]
print("\nHeights:", heights2)
print("Two pointers:", max_water(heights2))


heights3 = [4,3,2,1,4]
print("\nHeights:", heights3)
print("Two pointers:", max_water(heights3))


heights4 = [1,2,1]
print("\nHeights:", heights4)
print("Two pointers:", max_water(heights4))


# ------------------------------------------------------------
# Small Practice
# ------------------------------------------------------------
# 1. Return the maximum area and the two indices
#
# Example:
# [1,8,6,2,5,4,8,3,7]
#
# Answer could be:
# area = 49
# indices = [1, 8]
#
#
# 2. Print all areas checked by the brute force solution
#
#
# 3. Add print statements to the two pointer solution
# to see how left and right move
#
#
# 4. Try to explain in your own words:
# why do we move the shorter pointer?
#
#
# 5. Dry run this input by hand:
# [2,3,10,5,7,8,9]