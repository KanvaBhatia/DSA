# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def calc(self, b, op, a):
        if op == "+":
            return int(b) + int(a)
        if op == "-":
            return int(b) - int(a)
        if op == "*":
            return int(b) * int(a)
        if op == "/":
            return int(int(b) / int(a))
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ['+', '-', '*', '/']:
                stack.append(tokens[i])
            else:
                num_a = stack.pop()
                num_b = stack.pop()
                res = self.calc(num_b, tokens[i], num_a)
                stack.append(res)
        return int(stack.pop())
