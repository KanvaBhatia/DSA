# https://www.codingninjas.com/studio/problems/print-all-divisors-of-a-number_1164188
from typing import List

def printDivisors(n: int) -> List[int]:
    ans = []
    for i in range(1, n + 1):
        if n % i == 0:
            ans.append(i)
    return ans