# https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960

def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # larg = [-float('inf')] * 2
    a.remove(max(a))
    lg = max(a)
    a.remove(min(a))
    larg = [lg, min(a)]
    return larg
