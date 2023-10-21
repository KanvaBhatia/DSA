# https://www.codingninjas.com/studio/problems/hcf-and-lcm_840448
def calcGDC(n:int, m: int) -> int:
    if n == 0:
        return m
    if m > n:
        temp = m
        m = n
        n = temp
    return calcGDC(n % m, m)