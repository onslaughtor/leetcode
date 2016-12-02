'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n==0:
            return 0
        s0,s1,s2=0,-prices[0],0
        for i in xrange(1,n):
            tmp=s0
            s0=max(s0,s2)
            s2=s1+prices[i]
            s1=max(s1,tmp-prices[i])
        return max(s0,s1,s2)
        
                