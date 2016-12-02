'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
'''
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix)==0:
            return 0
        ans=[[-1]*len(matrix[0]) for i in xrange(len(matrix))]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if ans[i][j]==-1:
                    self.dfs(i,j,matrix,ans)
        ret=1
        for row in ans:
            for x in row:
                ret=max(ret,x)
        return ret
                    
    def dfs(self,x,y,matrix,ans):
        if ans[x][y]!=-1:
            return ans[x][y]
        ans[x][y]=1
        if self.check(matrix,x,y,x-1,y):
            ans[x][y]=max(ans[x][y],self.dfs(x-1,y,matrix,ans)+1)
        if self.check(matrix,x,y,x+1,y):
            ans[x][y]=max(ans[x][y],self.dfs(x+1,y,matrix,ans)+1)
        if self.check(matrix,x,y,x,y-1):
            ans[x][y]=max(ans[x][y],self.dfs(x,y-1,matrix,ans)+1)
        if self.check(matrix,x,y,x,y+1):
            ans[x][y]=max(ans[x][y],self.dfs(x,y+1,matrix,ans)+1)
        return ans[x][y]
        
    def check(self,matrix,x,y,xx,yy):
        return xx>=0 and xx<len(matrix) and yy>=0 and yy<len(matrix[xx]) and matrix[x][y]<matrix[xx][yy]