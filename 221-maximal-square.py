'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
'''
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ans=0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if i==0 or j==0:
                    matrix[i][j]=int(matrix[i][j])
                elif matrix[i][j]=='1':
                    matrix[i][j]=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1
                else:
                    matrix[i][j]=0
                ans=max(ans,matrix[i][j])
        return ans*ans 
        