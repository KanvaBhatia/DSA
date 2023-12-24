# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c_0 = nums.count(0)
        for _ in range(c_0):
            nums.remove(0)
        nums.extend([0] * c_0)
        