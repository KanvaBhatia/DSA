# https://www.codingninjas.com/studio/problems/print-1-to-n_628290
from  typing import *

def printNtimes(n: int) -> None:
    if n == 0:
        pass
    else:
        print("Coding Ninjas", end = " ")
        printNtimes(n - 1)