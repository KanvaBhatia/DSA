# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_diff = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > max_diff:
        #             max_diff = prices[j] - prices[i]
        # return max_diff
        max_p = 0
        min_n = float('inf')
        for i in range(len(prices)):
            min_n = min(min_n, prices[i])
            max_p = max(max_p, prices[i] - min_n)
        return max_p