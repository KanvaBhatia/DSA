# https://www.codingninjas.com/studio/problems/check-prime_624934
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
flag = 0
for i in range(2, int(sqrt(n) + 1)):
    if n % i == 0:
        flag = 1
        print('NO')
        break
if not flag and n != 1:
    print('YES')
elif n == 1:
    print("NO")