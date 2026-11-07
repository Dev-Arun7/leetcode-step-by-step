
"""
217. Contains Duplicate

Difficulty: Easy

Question:
Given an integer array nums, return True if any value appears
at least twice in the array, and return False if every element
is distinct.

Example 1:
Input: nums = [1, 2, 3, 1]
Output: True

Example 2:
Input: nums = [1, 2, 3, 4]
Output: False

Example 3:
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: True

LeetCode:
https://leetcode.com/problems/contains-duplicate/
"""

# --------------------------------------------------
# Solution
# --------------------------------------------------

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        contains_set = set()

        for num in nums:

            # Check whether the number already exists in the set
            if num in contains_set:
                return True

            # If not, add the number to the set
            else:
                contains_set.add(num)

        # No duplicate was found
        return False


# --------------------------------------------------
# Test
# --------------------------------------------------

solution = Solution()

nums = [1, 2, 3, 1]

result = solution.containsDuplicate(nums)

print(result)  # True

# --------------------------------------------------
# Notes
# --------------------------------------------------

"""
Approach: Hash Set

How does it work?

1. Create an empty set.
2. Loop through each number in the array.
3. Check whether the number already exists in the set.
4. If it exists, a duplicate is found. Return True.
5. Otherwise, add the number to the set.
6. If the loop finishes without finding a duplicate,
   return False.

Why use a set?

- A set stores only unique values.
- Checking whether a value exists in a set takes O(1)
  average time.
- This helps us find duplicates without comparing
  every element with every other element.

Time Complexity: O(n)
    In the worst case, we visit every element once.

Space Complexity: O(n)
    In the worst case, the set stores all n elements.
"""
