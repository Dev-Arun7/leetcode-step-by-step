
"""
242. Valid Anagram

Difficulty: Easy

Question:
Given two strings s and t, return True if t is an anagram
of s, and False otherwise.

An anagram contains exactly the same characters with
the same frequency.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: True

Example 2:
Input: s = "rat", t = "car"
Output: False

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

Follow-up:
What if the inputs contain Unicode characters?

LeetCode:
https://leetcode.com/problems/valid-anagram/
"""


# --------------------------------------------------
# Approach 1: Hash Map (Frequency Counting)
# --------------------------------------------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Different lengths cannot be anagrams
        if len(s) != len(t):
            return False

        s_freq = {}
        t_freq = {}

        # Count the frequency of each character in s
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1

        # Count the frequency of each character in t
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        # Both frequency dictionaries must be equal
        return s_freq == t_freq


# --------------------------------------------------
# Approach 2: Character Frequency Array
# --------------------------------------------------

class SolutionArray:
    def isAnagram(self, s: str, t: str) -> bool:

        # Different lengths cannot be anagrams
        if len(s) != len(t):
            return False

        # Create an array with 26 zeros (a to z)
        char_count = [0] * 26

        for i in range(len(s)):

            # Increase count for characters in s
            char_count[ord(s[i]) - ord('a')] += 1

            # Decrease count for characters in t
            char_count[ord(t[i]) - ord('a')] -= 1

        # All counts should be zero if both strings are anagrams
        for count in char_count:
            if count != 0:
                return False

        return True


# --------------------------------------------------
# Notes
# --------------------------------------------------

"""
Approach 1: Hash Map (Frequency Counting)

How it works:
1. Check whether both strings have the same length.
2. Create two empty dictionaries.
3. Count each character in the first string.
4. Count each character in the second string.
5. Compare both dictionaries.
6. If they are equal, both strings are anagrams.

Why this approach?
Dictionaries store characters as keys and their frequencies
as values. Comparing both dictionaries verifies that every
character occurs the same number of times.

Time Complexity: O(n)
Space Complexity: O(1) under the given lowercase alphabet constraint.


Approach 2: Character Frequency Array

How it works:
1. Check whether both strings have the same length.
2. Create an array containing 26 zeros.
3. Increase the count for each character in s.
4. Decrease the count for each character in t.
5. Check whether all array values are zero.
6. If all values are zero, both strings are anagrams.

Why this approach?
Instead of using dictionaries, we use an array of fixed size.
Each lowercase English letter has its own index.

ord('a') - ord('a') = 0
ord('b') - ord('a') = 1
ord('z') - ord('a') = 25

Time Complexity: O(n)
Space Complexity: O(1) - fixed array of 26 elements.


Comparison:

Hash Map:
- Easy to understand.
- Supports different character sets.
- Uses dictionaries to store frequencies.

Frequency Array:
- Uses a fixed-size array.
- Avoids dictionary creation and comparison.
- Works for lowercase English letters only.

Unicode Follow-up:
For Unicode characters, the 26-element array is not suitable.
A dictionary-based frequency count can support Unicode characters.
"""


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    s = "anagram"
    t = "nagaram"

    # Test Approach 1
    solution = Solution()
    result = solution.isAnagram(s, t)
    print("Hash Map:", result)

    # Test Approach 2
    solution_array = SolutionArray()
    result = solution_array.isAnagram(s, t)
    print("Frequency Array:", result)
