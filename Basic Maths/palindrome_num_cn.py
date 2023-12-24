# https://www.codingninjas.com/studio/problems/palindrome-number_624662
n = input()
# taking n as a input 
## write your code !!

if n == n[::-1]:
    print('true')
else:
    print("false")