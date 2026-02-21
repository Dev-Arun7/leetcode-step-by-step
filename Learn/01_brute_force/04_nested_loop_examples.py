"""
What you learn:
- How nested loops work
- Different common nested loop patterns
- When we use i, j
- How time complexity becomes O(n^2)

Why this matters:
- Many brute force solutions use nested loops
- Understanding loop patterns helps in pair problems,
  comparison problems, matrix problems, etc.
"""


# ------------------------------------------------------------
# Example 1: Print all pairs (i, j)
# Time: O(n^2)
# ------------------------------------------------------------
def print_all_pairs(nums):
    print("All pairs (including same index):")

    for i in range(len(nums)):
        for j in range(len(nums)):
            print(f"({nums[i]}, {nums[j]})") # Keep attention here


# ------------------------------------------------------------
# Example 2: Print unique pairs (i < j)
# Time: O(n^2)
# This is the pattern used in pair sum brute force
# ------------------------------------------------------------
def print_unique_pairs(nums):
    print("Unique pairs (i < j):")

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print("(", nums[i], ",", nums[j], ")")


# ------------------------------------------------------------
# Example 3: Compare each element with others
# Used in duplicate checking
# ------------------------------------------------------------
def check_duplicates_bruteforce(nums):
    print("Checking duplicates:")

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                print("Duplicate found:", nums[i])


# ------------------------------------------------------------
# Example 4: Triangle pattern (growing inner loop)
# Common in pattern problems
# ------------------------------------------------------------
def triangle_pattern(n):
    print("Triangle pattern:")

    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()  # new line


# ------------------------------------------------------------
# Example 5: Counting operations (to understand O(n^2))
# ------------------------------------------------------------
def count_operations(n):
    count = 0

    for i in range(n):
        for j in range(n):
            count += 1

    print("Total operations for n =", n, "is", count)


# ------------------------------------------------------------
# Run examples
# ------------------------------------------------------------
nums = [1, 2, 3]

print_all_pairs(nums)
print()

print_unique_pairs(nums)
print()

check_duplicates_bruteforce([1, 2, 3, 2, 1])
print()

triangle_pattern(4)
print()

count_operations(3)