class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif i in [')', ']', '}']:
                if stack and stack[-1] == close_open[i]:
                    stack.pop()
                else:
                    return False
        return stack == []