# https://www.codingninjas.com/studio/problems/sum-of-first-n-numbers_8876068


# correct recursive call
from typing import List

def sumFirstN(n: int) -> int:
    if n != 0:
        return n + sumFirstN(n - 1)
    else:
        return 0


# correct but formula used
from typing import List

def sumFirstN(n: int) -> int:
    return int((n / 2) * (1 + n))