# https://www.codingninjas.com/studio/problems/selection-sort_624469
from typing import List

def selectionSort(arr: List[int]) -> None: 
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp