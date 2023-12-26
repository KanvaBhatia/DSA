# https://leetcode.com/problems/two-sum


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i,j]
        hash_table = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hash_table:
                return [hash_table[comp], i]
            hash_table[nums[i]] = i