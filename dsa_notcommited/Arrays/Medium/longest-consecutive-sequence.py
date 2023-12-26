# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        for num in nums:
            temp = num
            temp_long = 0
            while (temp in nums) and (num - 1 not in nums):
                temp_long += 1
                temp += 1
            longest = max(temp_long, longest)
        return longest
        
