class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = {}
        t_freq = {}
        for letter in s:
            s_freq[letter] = s_freq.get(letter, 0) + 1
        for letter in t:
            t_freq[letter] = t_freq.get(letter, 0) + 1

        for key, value in s_freq.items():
            if t_freq.get(key, None) and t_freq.get(key, None) == value:
                continue
            else:
                return False
        

obj = Solution()
s = "anagram"
t = "nagaram"
result = obj.isAnagram(s, t)


print(result)

