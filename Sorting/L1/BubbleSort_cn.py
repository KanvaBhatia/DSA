# https://www.codingninjas.com/studio/problems/bubble-sort_624380

from typing import List

def bubbleSort(arr: List[int], n: int):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp