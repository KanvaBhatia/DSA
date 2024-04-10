# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        temp = temperatures
        stack = []
        for i, t in enumerate(temp):
            while stack and t > stack[-1][0]:
                elem, ind = stack.pop()
                output[ind] = i - ind
            stack.append([t, i])
        return output
