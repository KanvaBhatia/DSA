# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        while i < m and target > matrix[i][-1]:
            i += 1
        if i >= m:
            return False
        row = matrix[i]
        l, r = 0, n - 1
        while l <= r:
            m = l + (r-l) // 2
            if target == row[m]:
                return True
            elif target < row[m]:
                r = m - 1
            elif target > row[m]:
                l = m + 1
        return False
