"""
49. Group Anagrams

Difficulty: Medium

Question:
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

Anagrams are words that contain the same characters
with the same frequency.

Example 1:
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

LeetCode:
https://leetcode.com/problems/group-anagrams/
"""


# --------------------------------------------------
# Approach 1: Character Frequency Array + Hash Map
# --------------------------------------------------

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anagrams = {}

        for word in strs:

            # Create an array of 26 zeros (a to z)
            char_count = [0] * 26

            # Count the frequency of each character
            for char in word:
                char_count[ord(char) - ord('a')] += 1

            # Convert the list into a tuple (tuples can be dictionary keys)
            key = tuple(char_count)

            # Create a new group if the key does not exist
            if key not in anagrams:
                anagrams[key] = []

            # Add the original word to its matching group
            anagrams[key].append(word)

        # Return all grouped anagrams
        return list(anagrams.values())


# --------------------------------------------------
# Notes
# --------------------------------------------------

"""
Approach 1: Character Frequency Array + Hash Map

How it works:
1. Create an empty dictionary.
2. Loop through each word in the input list.
3. Create an array containing 26 zeros.
4. Count the frequency of each character in the word.
5. Convert the frequency array into a tuple.
6. Use the tuple as the dictionary key.
7. If the key does not exist, create an empty list.
8. Append the original word to that dictionary key.
9. Return all dictionary values as a list.

Why this approach?

Anagrams contain exactly the same characters with
the same frequencies.

For example:

"eat" -> [1, 0, 0, 0, 1, 0, ..., 1, ...]

"tea" -> [1, 0, 0, 0, 1, 0, ..., 1, ...]

Both words produce the same frequency array.

Therefore, they produce the same tuple and dictionary key.

Words with the same dictionary key belong to the same group.


Important Concepts:

1. Character Frequency Array:

   char_count = [0] * 26

   Creates an array with 26 zeros, representing
   lowercase English letters from a to z.

2. ord():

   ord('a') = 97
   ord('b') = 98
   ord('z') = 122

   ord(char) - ord('a') gives the character's index.

   Example:
   ord('e') - ord('a') = 4

3. Tuple:

   key = tuple(char_count)

   Lists cannot be used as dictionary keys because
   lists are mutable.

   Tuples are immutable, so they can be used as
   dictionary keys.

4. Dictionary:

   anagrams[key] = []

   Creates a new group for a character frequency pattern.

   anagrams[key].append(word)

   Adds the original word to its matching group.


Time Complexity: O(n * k)

- n = Number of words.
- k = Maximum length of a word.
- We process each character once.
- Creating and converting the frequency array takes
  constant time because it always contains 26 elements.

Space Complexity: O(n * k)

- The dictionary stores all input words in groups.
- Each group uses a tuple of 26 elements as its key.
- Since the alphabet size is fixed, the auxiliary
  space for each key is constant.

Note:
This approach works for lowercase English letters only.
The problem constraints guarantee this condition.
"""


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    solution = Solution()
    result = solution.groupAnagrams(strs)

    print("Grouped Anagrams:", result)