# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest_substr = 0
        # for i in range(0, len(s) - longest_substr):
        #     substr = ""
        #     j = 0
        #     while (i + j) < len(s) and s[i + j] not in substr:
        #         substr += s[i + j]
        #         j += 1
        #         longest_substr = max(longest_substr, len(substr)) 
        # return longest_substr


        seen = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, len(seen))
        return res
    