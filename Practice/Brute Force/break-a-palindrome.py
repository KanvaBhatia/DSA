# https://leetcode.com/problems/break-a-palindrome/

# TOOD NOT GOOD SOLN
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        answer = ""
        flag = False
        for i in range(len(palindrome)):
            if not flag and palindrome[i] != 'a':
                answer += "a"
                flag = True
            else:
                answer += palindrome[i]
        # if palindrome == answer or ((len(palindrome) % 2 != 0) amd (palindrome[0 : int(len(palindrome) / 2)] == palindrome[(int(len(palindrome) / 2) + 1):]) ):
        if palindrome == answer or ((len(palindrome) % 2 != 0) and (palindrome[0 : int(len(palindrome) / 2)] == palindrome[(int(len(palindrome) / 2) + 1):])):
            answer = palindrome[:-1] + "b"
        if palindrome == answer:
            answer = ""
            flag = False
            for i in range(len(palindrome)):
                if not flag and palindrome[i] != 'a':
                    answer += "a"
                    flag = True
                else:
                    answer += palindrome[i]
        return answer
        