# https://www.codingninjas.com/studio/problems/largest-element-in-the-array-largest-element-in-the-array_5026279

from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:

    larg = -float('inf')
    for i in arr:
        if i > larg:
            larg = i

    return larg