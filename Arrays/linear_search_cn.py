# https://www.codingninjas.com/studio/problems/linear-search_6922070

def linearSearch(n: int, num: int, arr: [int]) -> int:
    for i in range(n):
        if arr[i] == num:
            return i
    return -1
