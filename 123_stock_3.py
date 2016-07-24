'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        post_profit=[0]*(len(prices)+1)
        post_max=prices[-1]
        for i in range(len(prices)-2,0,-1):
            post_profit[i]=max(post_profit[i+1],post_max-prices[i])
            post_max=max(post_max,prices[i])
        pre_min=prices[0]
        ans=0
        for i in range(1,len(prices)):
            ans=max(ans,prices[i]-pre_min+post_profit[i+1])
            pre_min=min(pre_min,prices[i])
        return ans 
