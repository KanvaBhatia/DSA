# https://www.codingninjas.com/studio/problems/insertion-sort_624381

# recursive - 
# https://www.geeksforgeeks.org/recursive-insertion-sort/#


# non recursive - 
from typing import List

def insertionSort(a: List[int], n: int) -> None:
   for i in range(n):
      j = i
      while j > 0 and a[j - 1] > a[j]:
         temp = a[j-1]
         a[j-1] = a[j]
         a[j] = temp
         j -= 1