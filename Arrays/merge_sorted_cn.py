# https://www.codingninjas.com/studio/problems/sorted-array_6613259

def sortedArray(a: [int], b: [int]) -> [int]:
    return sorted(list(set(a + b)))
