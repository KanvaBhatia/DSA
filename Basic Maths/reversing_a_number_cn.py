# https://www.codingninjas.com/studio/problems/reverse-bits_2181102
def reverseBits(n):
    rev = ""
    temp = n
    while temp > 0:
        rev += "0" if temp % 2 == 0 else "1"
        temp = int(temp / 2)
    rev = rev[::-1]
    rev = "0" * (32 - len(rev)) + rev
    rev_int = int(rev[::-1], 2)
    return rev_int

