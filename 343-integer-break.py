'''
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
'''
class Solution(object):
    dp=[0,1]
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in xrange(len(self.dp),n+1):
            self.dp.append(0)
            for j in xrange(1,i):
               self.dp[i]=max(self.dp[i],max(j,self.dp[j])*(i-j))
        return self.dp[n]
        