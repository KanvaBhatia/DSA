# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # zero = [0]
        # zero.extend(digits)
        # carry = 1
        # for i in range(len(zero) - 1, -1, -1):
        #     zero[i] += carry
        #     if zero[i] >= 10:
        #         carry = 1
        #         zero[i] %= 10
        #     else:
        #         carry = 0
        # if zero[0] == 0:
        #     zero.remove(0)
        # return zero


        # dig = [str(i) for i in digits]
        # sum_d = str(int("".join(dig)) + 1)
        # res = [int(i) for i in sum_d]
        # return res

        one = 1
        digits = digits[::-1]
        i = 0
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1]