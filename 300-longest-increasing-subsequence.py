'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last=[]
        for i in nums:
            left,right=0,len(last)-1
            while left<=right:
                mid=(left+right)>>1
                if last[mid]<i:
                    left=mid+1
                else:
                    right=mid-1
            if left<len(last):
                last[left]=i
            else:
                last.append(i)
        return len(last)