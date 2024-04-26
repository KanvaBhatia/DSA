# https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = l + (r - l) // 2
            hrs = 0
            for p in piles:
                hrs += math.ceil(p / m)
            if hrs <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        return res