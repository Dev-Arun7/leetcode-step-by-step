
"""
1. Two Sum

Difficulty: Easy

Question:
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up
to the target.

You may assume that each input would have exactly one
solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Example 3:
Input: nums = [3, 3], target = 6
Output: [0, 1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

LeetCode:
https://leetcode.com/problems/two-sum/
"""


# --------------------------------------------------
# Approach 1: Brute Force (Nested Loops)
# --------------------------------------------------

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # Check every possible pair of numbers
        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):

                # Check whether the pair adds up to target
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []


# --------------------------------------------------
# Approach 2: Hash Map (One Pass)
# --------------------------------------------------

class SolutionHashMap:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # Store numbers and their indices
        num_map = {}

        for i in range(len(nums)):

            # Find the number needed to reach the target
            required = target - nums[i]

            # Check whether the required number already exists
            if required in num_map:
                return [num_map[required], i]

            # Store the current number and its index
            num_map[nums[i]] = i

        return []


# --------------------------------------------------
# Notes
# --------------------------------------------------

"""
Approach 1: Brute Force (Nested Loops)

How it works:
1. Use the first loop to select a number.
2. Use the second loop to select another number.
3. Make sure the second index is always greater than
   the first index.
4. Add both numbers and compare their sum with target.
5. If the sum matches, return their indices.

Why this approach?
We check every possible pair of numbers until we find
the pair that adds up to the target.

Time Complexity: O(n^2)
Space Complexity: O(1)


Approach 2: Hash Map (One Pass)

How it works:
1. Create an empty dictionary.
2. Loop through the array.
3. Calculate the required number:

   required = target - nums[i]

4. Check whether the required number exists in the dictionary.
5. If it exists, return its stored index and the current index.
6. Otherwise, store the current number and its index.
7. Continue until the pair is found.

Why this approach?
Instead of checking every possible pair, we use a dictionary
to remember previously visited numbers and their indices.

This allows us to find the required number quickly.

Example:

nums = [2, 7, 11, 15]
target = 9

Iteration 1:
Current number = 2
Required number = 9 - 2 = 7
7 is not in the dictionary.

Store: {2: 0}

Iteration 2:
Current number = 7
Required number = 9 - 7 = 2
2 already exists in the dictionary.

Return [0, 1]

Time Complexity: O(n) - average case
Space Complexity: O(n)


Comparison:

Brute Force:
- Uses nested loops.
- Checks every possible pair.
- Simple to understand.
- Slower for large arrays.

Hash Map:
- Uses a dictionary.
- Stores previously visited numbers and indices.
- Finds the required number using dictionary lookup.
- Much faster than brute force for large arrays.

Important Concepts:
- Nested loops
- Dictionary
- Dictionary lookup using `in`
- Storing key-value pairs
- Complement calculation (target - current number)
"""


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    nums = [2, 7, 11, 15]
    target = 9

    # Test Approach 1
    solution = Solution()
    result = solution.twoSum(nums, target)
    print("Brute Force:", result)

    # Test Approach 2
    solution_hash_map = SolutionHashMap()
    result = solution_hash_map.twoSum(nums, target)
    print("Hash Map:", result)
