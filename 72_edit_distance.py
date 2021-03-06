'''
Given two words word1 and word2, 
find the minimum number of steps(Insert, Delete, Replace) required to convert word1 to word2
'''
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n=len(word1)
        m=len(word2)
        dp=[[1]*(m+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][0]=i
        for i in range(m+1):
            dp[0][i]=i
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
        return dp[n][m]