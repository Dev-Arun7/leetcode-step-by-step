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

            # Group words with the same character frequencies
            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(word)

        return list(anagrams.values())