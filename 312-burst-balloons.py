'''
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.
'''
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        nums=[1]+nums+[1]
        dp=[[0]*(n+2) for i in xrange(n+2)]
        for k in xrange(1,n+1):
            for i in xrange(1,n-k+2):
                for j in xrange(i,i+k):
                    dp[i][i+k-1]=max(dp[i][i+k-1],dp[i][j-1]+dp[j+1][i+k-1]+nums[j]*nums[i-1]*nums[i+k])
        return dp[1][n]
        
                    
                