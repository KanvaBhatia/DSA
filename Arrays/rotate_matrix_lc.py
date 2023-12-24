# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        import numpy
        matrix[:] = numpy.matrix(matrix).transpose().tolist()
        for row in matrix:
            row.reverse()