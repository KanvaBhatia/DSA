# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        rem = 0
        num = x
        x = abs(x)
        if x == 0: return 0
        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x = x // 10
        rev = int(rev * num / abs(num))
        return rev if rev >= -2 ** 31 and rev <= 2 ** 31 - 1 else 0
