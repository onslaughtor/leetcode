class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if k*2>=n:
            return self.maxProfitN(prices)
        dp=[[0]*(k+1) for i in xrange(n)]
        for j in xrange(1,k+1):
            tmp=-prices[0]
            for i in xrange(1,n):
                dp[i][j]=max(dp[i-1][j],prices[i]+tmp)
                tmp=max(tmp,dp[i-1][j-1]-prices[i])
        return dp[-1][-1]

    def maxProfitN(self,prices):
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
        return profit