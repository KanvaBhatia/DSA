# https://www.codingninjas.com/studio/problems/count-digits_8416387

def countDigits(n: int) -> int:
    count = 0
    for c in str(n):
        if int(c) != 0 and n % int(c) == 0:
            count += 1
    return count
    