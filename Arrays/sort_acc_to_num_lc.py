# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums.count(0)*[0] + nums.count(1) * [1] + nums.count(2) * [2]