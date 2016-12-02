'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[-1]*(amount+1)
        dp[0]=0
        for i in xrange(1,amount+1):
            for j in coins:
                if i-j<0:
                    continue
                if dp[i-j]>-1 and (dp[i]==-1 or dp[i-j]+1<dp[i]):
                    dp[i]=dp[i-j]+1
        return dp[-1]