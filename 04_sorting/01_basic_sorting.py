"""
basic_sorting.py

What you will learn:
- What sorting algorithms do step by step
- How Bubble Sort works
- How Selection Sort works
- Why Python's built-in sort is usually better

*Important*: 
In real problems, you should usually use Python's built-in sorting.

But learning simple sorting algorithms helps you understand:
- comparisons
- swaps
- passes
- how sorting actually happens
"""


# ------------------------------------------------------------
# Bubble Sort
# ------------------------------------------------------------
# Idea:
# Compare neighboring elements.
# If they are in the wrong order, swap them.
#
# Bigger values slowly "bubble up" to the end.
#
# Example:
# [5, 2, 8, 1]
#
# Compare 5 and 2 -> swap
# [2, 5, 8, 1]
#
# Compare 5 and 8 -> no swap
# [2, 5, 8, 1]
#
# Compare 8 and 1 -> swap
# [2, 5, 1, 8]
#
# After one full pass, the largest value is at the end.


def bubble_sort(nums):
    arr = nums.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# ------------------------------------------------------------
# Bubble Sort with step display
# ------------------------------------------------------------
# This version prints what is happening.
# Good for learning.

def bubble_sort_with_steps(nums):
    arr = nums.copy()
    n = len(arr)

    print("\nBubble Sort Steps")
    print("Start:", arr)

    for i in range(n):
        print(f"\nPass {i + 1}")
        swapped = False

        for j in range(0, n - 1 - i):
            print(f"Compare {arr[j]} and {arr[j + 1]}")

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print("Swap  ->", arr)
            else:
                print("No swap ->", arr)

        if not swapped:
            print("No swaps in this pass, list is already sorted.")
            break

    print("\nFinal sorted list:", arr)
    return arr


# ------------------------------------------------------------
# Selection Sort
# ------------------------------------------------------------
# Idea:
# Find the smallest value and place it at the front.
#
# Then find the next smallest value and place it next.
#
# Example:
# [5, 2, 8, 1]
#
# Smallest is 1, swap with first position:
# [1, 2, 8, 5]
#
# Then find smallest in remaining part:
# [2, 8, 5] -> 2 is already correct
#
# Then:
# [8, 5] -> smallest is 5
# [1, 2, 5, 8]

def selection_sort(nums):
    arr = nums.copy()
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# ------------------------------------------------------------
# Selection Sort with step display
# ------------------------------------------------------------
def selection_sort_with_steps(nums):
    arr = nums.copy()
    n = len(arr)

    print("\nSelection Sort Steps")
    print("Start:", arr)

    for i in range(n):
        min_index = i
        print(f"\nPosition {i}: looking for smallest value from index {i} to end")

        for j in range(i + 1, n):
            print(f"Compare current smallest {arr[min_index]} with {arr[j]}")
            if arr[j] < arr[min_index]:
                min_index = j
                print(f"New smallest found: {arr[min_index]} at index {min_index}")

        arr[i], arr[min_index] = arr[min_index], arr[i]
        print("After placing smallest at correct position:", arr)

    print("\nFinal sorted list:", arr)
    return arr


# ------------------------------------------------------------
# Learning Note
# ------------------------------------------------------------
# Bubble Sort:
# - repeatedly swaps neighboring elements
# - larger values move to the right
#
# Selection Sort:
# - repeatedly selects the smallest remaining value
# - places it in the correct position
#
# Both are useful for learning,
# but not the best choice for real coding interview problems.


# ------------------------------------------------------------
# Time Complexity
# ------------------------------------------------------------
# Bubble Sort:
# Time: O(n^2)
# Space: O(1) if sorting in place
#
# Selection Sort:
# Time: O(n^2)
# Space: O(1) if sorting in place
#
# Python built-in sort:
# Much better in practice
# Around O(n log n)


# ------------------------------------------------------------
# Beginner Mistakes
# ------------------------------------------------------------
# 1. Changing the original list by accident
#
#    That is why this script uses nums.copy()
#
# 2. Forgetting the inner loop becomes shorter in Bubble Sort
#
#    After each pass, the largest value is already at the end
#
# 3. Confusing index and value
#
#    i, j, min_index are positions
#    arr[i], arr[j] are values
#
# 4. Thinking these are the best sorting methods for interviews
#
#    They are great for learning
#    but built-in sort is usually better in real problems


# ------------------------------------------------------------
# Runnable Examples
# ------------------------------------------------------------
nums1 = [5, 2, 8, 1, 3]

print("Original list:", nums1)
print("Bubble Sort result:", bubble_sort(nums1))
print("Selection Sort result:", selection_sort(nums1))
print("Original list still unchanged:", nums1)

nums2 = [9, 4, 7, 2]
print("\nOriginal list:", nums2)
print("Bubble Sort result:", bubble_sort(nums2))
print("Selection Sort result:", selection_sort(nums2))

nums3 = [1, 2, 3, 4]
print("\nOriginal list:", nums3)
print("Bubble Sort result:", bubble_sort(nums3))
print("Selection Sort result:", selection_sort(nums3))

nums4 = [4, 4, 2, 1, 2]
print("\nOriginal list:", nums4)
print("Bubble Sort result:", bubble_sort(nums4))
print("Selection Sort result:", selection_sort(nums4))


# ------------------------------------------------------------
# Step-by-step Demo
# ------------------------------------------------------------
bubble_sort_with_steps([5, 2, 8, 1])
selection_sort_with_steps([5, 2, 8, 1])


# ------------------------------------------------------------
# Python Built-in Sorting
# ------------------------------------------------------------
# In real problems, this is what you will usually use.

nums5 = [6, 3, 9, 1]
print("\nBuilt-in sorted():", sorted(nums5))

nums5.sort()
print("Built-in list.sort():", nums5)


# ------------------------------------------------------------
# Small Practice
# ------------------------------------------------------------
# 1. Change bubble_sort to sort in descending order
#
# 2. Change selection_sort to sort in descending order
#
# 3. Count how many swaps Bubble Sort makes
#
# 4. Count how many comparisons Selection Sort makes
#
# 5. Try sorting:
#    [10, 7, 8, 3, 2]
#
#    by hand before running the code