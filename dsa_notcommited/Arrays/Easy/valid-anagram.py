# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in t:
                t = t.replace(s[i], ".", 1)
                # print(t)
            else:
                return False
        return True
