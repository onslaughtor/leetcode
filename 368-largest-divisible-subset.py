'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.
'''
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []
        nums.sort()
        dp=[1]*len(nums)
        pre=[i for i in xrange(len(nums))]
        
        for i in xrange(len(nums)):
            for j in xrange(i-1,-1,-1):
                if nums[i]%nums[j]==0 and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    pre[i]=j
        idx=dp.index(max(dp))
        ans=[nums[idx]]
        while pre[idx]!=idx:
            idx=pre[idx]
            ans.append(nums[idx])
        return ans
            