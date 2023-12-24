# https://www.codingninjas.com/studio/problems/check-armstrong_589
from os import *
from sys import *
from collections import *
from math import *

n = str(input())
sum = 0
for num in n:
    sum += int(num) ** len(n)

if str(sum) == n:
    print('true')
else:
    print('false')