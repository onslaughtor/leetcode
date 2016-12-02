'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0:
            return False
        x,y=0,len(matrix[0])-1
        while x<len(matrix) and y>=0:
            if matrix[x][y]==target:
                return True
            elif matrix[x][y]>target:
                y-=1
            else:
                x+=1
        return False
            
        