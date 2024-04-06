# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif i in [')', ']', '}']:
                if stack[-1] != close_open[i]:
                    return False
                else:
                    stack.pop()
        return True