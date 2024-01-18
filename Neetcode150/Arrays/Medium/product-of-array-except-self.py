# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix_prod = [nums[0]] + [0] * (len(nums) - 1)
        # postfix_prod = [0] * (len(nums) - 1) + [nums[-1]]
        # for i in range(1, len(nums)):
        #     prefix_prod[i] = prefix_prod[i - 1] * nums[i]
        # for i in range(len(nums) - 2, -1, -1):
        #     postfix_prod[i] = postfix_prod[i + 1] * nums[i]
        # res = [postfix_prod[1]]
        # for i in range(1, len(nums) - 1):
        #     res.append(prefix_prod[i - 1] * postfix_prod[i + 1])
        # res.append(prefix_prod[-2])
        # return res

        output =[1] * len(nums)

        pre,post=1,1

        for i in range(len(nums)):
            output[i] *= pre
            pre *= nums[i]
        for j in range(len(nums)-1,-1,-1):
             output[j] *= post
             post *= nums[j]
        return output