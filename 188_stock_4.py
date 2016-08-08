'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.
Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

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
        trans=[0]*(k+1)
        dp=[0]*(k+1)
        for i in xrange(1,n):
            diff=prices[i]-prices[i-1]
            for j in xrange(1,k+1):
                trans[j]=max(trans[j]+diff,dp[j-1])
                dp[j]=max(dp[j],trans[j])
        return max(dp)

    def maxProfitN(self,prices):
        profit=0
        p=-1
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1] and p==-1:
                p=prices[i]
            if  prices[i]>prices[i+1] and p>-1:
                profit+=(prices[i]-p)
                p=-1
        if len(prices)>0 and p>-1:
            profit+=prices[-1]-p
        return profit

'''
Solution: can not understand this solution completely
Type: DP,Greedy
Inspiration: 
'''