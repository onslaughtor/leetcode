'''
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.
'''
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        m=0
        cnt=0
        for i in nums:
            if m>=n:
                break
            while m<n and m<i-1:
                cnt+=1
                m=m*2+1
            m+=i
        while m<n:
            cnt+=1
            m=m*2+1
        return cnt
                
            
        