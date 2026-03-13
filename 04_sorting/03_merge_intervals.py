"""
What you will learn:
- Why sorting is useful for interval problems
- How to merge overlapping intervals
- How to scan a list and update the current interval

Problem:
You are given a list of intervals.

Each interval has:
[start, end]

Example:
[1,3] means it starts at 1 and ends at 3.

If two intervals overlap, we merge them.

Example:

Input:
[[1,3], [2,6], [8,10], [15,18]]

Output:
[[1,6], [8,10], [15,18]]

Explanation:

[1,3] and [2,6] overlap
so we merge them into [1,6]
"""


# ------------------------------------------------------------
# Why sorting helps
# ------------------------------------------------------------
# If intervals are not sorted, merging is difficult.
#
# Example:
#
# [[8,10], [1,3], [2,6]]
#
# Sorting by start value gives:
#
# [[1,3], [2,6], [8,10]]
#
# Now overlapping intervals appear next to each other.


# ------------------------------------------------------------
# Solution
# ------------------------------------------------------------
# Steps:
#
# 1. Sort intervals by start value
# 2. Start with the first interval
# 3. Compare with the next interval
#
# If they overlap:
# merge them
#
# If not:
# add the previous interval to result


def merge_intervals(intervals):

    if not intervals:
        return []

    # Step 1: sort intervals
    intervals.sort()

    merged = []

    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:

        # Check overlap
        if start <= current_end:

            # Extend the interval
            current_end = max(current_end, end)

        else:

            # No overlap → save current interval
            merged.append([current_start, current_end])

            current_start = start
            current_end = end

    # Add the last interval
    merged.append([current_start, current_end])

    return merged


# ------------------------------------------------------------
# Step-by-step example
# ------------------------------------------------------------
# Input:
#
# [[1,3], [2,6], [8,10], [15,18]]
#
# After sorting:
#
# [[1,3], [2,6], [8,10], [15,18]]
#
# Compare:
#
# [1,3] and [2,6]
# overlap → merge → [1,6]
#
# Next:
#
# [8,10]
# no overlap → store [1,6]
#
# Continue...


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# This problem teaches a powerful pattern:
#
# 1. Sort data first
# 2. Scan the list
# 3. Merge or update while scanning
#
# Many problems use this idea.


# ------------------------------------------------------------
# Beginner mistakes
# ------------------------------------------------------------
# 1. Forgetting to sort intervals first
#
# 2. Not adding the last interval to the result
#
# 3. Using wrong overlap condition
#
# Correct check:
#
# start <= current_end
#
# If true → intervals overlap


# ------------------------------------------------------------
# Runnable examples
# ------------------------------------------------------------
example1 = [[1,3], [2,6], [8,10], [15,18]]
print("Input:", example1)
print("Merged:", merge_intervals(example1))


example2 = [[1,4], [4,5]]
print("\nInput:", example2)
print("Merged:", merge_intervals(example2))


example3 = [[1,10], [2,3], [4,8]]
print("\nInput:", example3)
print("Merged:", merge_intervals(example3))


example4 = []
print("\nInput:", example4)
print("Merged:", merge_intervals(example4))


# ------------------------------------------------------------
# Small Practice
# ------------------------------------------------------------
# 1. Count how many merged intervals exist
#
# Example:
# [[1,3], [2,6], [8,10]]
#
# Result intervals:
# [[1,6], [8,10]]
#
# Answer → 2
#
#
# 2. Return the total covered length
#
# Example:
# [[1,3], [2,6]]
#
# Merged:
# [[1,6]]
#
# Total length = 5
#
#
# 3. Detect if any intervals overlap
#
# Return True or False
#
#
# 4. Try solving without sorting first
# and see why sorting is important.