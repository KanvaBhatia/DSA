# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

class Solution:
    def check(self, nums: List[int]) -> bool:
        temp = nums.copy()
        temp.sort()
        for i in range(len(temp)):
            if nums[-i:] + nums[:-i] == temp:
                return True

        return False