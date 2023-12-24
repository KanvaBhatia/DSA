# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # My sol - 

        # temp = sorted(nums)
        # for i in range(len(temp) - 1):
        #     if temp[i] + 1 != temp[i + 1]:
        #         return temp[i] + 1
                
        # if temp[0] == 0:
        #     return len(temp)
        # else:
        #     return 0

        # Better sol - 
        sum_of_nums = sum(nums)
        supposed_to_be = (len(nums) * (len(nums) + 1)) / 2
        return int(supposed_to_be - sum_of_nums)