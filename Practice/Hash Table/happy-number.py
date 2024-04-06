# https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        hash_table = defaultdict(int)
        sum_n = n
        while sum_n != 1:
            new_sum = 0
            for i in str(sum_n):
                new_sum += int(i) ** 2
            sum_n = new_sum
            if hash_table[sum_n] != 0:
                return False
            else:
                hash_table[sum_n] = 1
        return True