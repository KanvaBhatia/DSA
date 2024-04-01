# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # srt = sorted([l for l in s1])
        # for i in range(0, len(s2)):
        #     st = sorted([l for l in s2[i: i + len(s1)]])
        #     if  srt == st:
        #         return True
        # return False
        
        if len(s1) > len(s2):
            return False
            
        hs1 = [0] * 26
        hs2 = [0] * 26

        for i in range(len(s1)):
            hs1[ord(s1[i]) - ord('a')] += 1
            hs2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if hs1[i] == hs2[i]:
                matches += 1
            
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            hs2[index] += 1
            if hs1[index] == hs2[index]:
                matches += 1
            elif hs1[index] + 1 == hs2[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            hs2[index] -= 1
            if hs1[index] == hs2[index]:
                matches += 1
            elif hs1[index] - 1 == hs2[index]:
                matches -= 1   
            l += 1
        return matches == 26