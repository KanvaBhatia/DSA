# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # mode = 0
        # for i in range(len(nums)):
        #     if
        f = sorted(nums)
        return f[len(f) // 2]