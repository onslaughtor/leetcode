class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res=[[0]*n for i in range(n)]
        k=1

        for i in range(n/2):
            for j in range(i,n-1-i):
                res[i][j]=k
                k+=1
            for j in range(i,n-1-i):
                res[j][n-1-i]=k
                k+=1   
            for j in range(n-1-i,i,-1):
                res[n-i-1][j]=k
                k+=1
            for j in range(n-i-1,i,-1):
                res[j][i]=k
                k+=1
        if n%2>0:
            res[n/2][n/2]=k
        return res

print Solution().generateMatrix(0)