'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=1
        right=len(nums)
        while left<=right:
            mid=(left+right)/2
            cnt=0
            tmp=0
            for i in nums:
                if i==mid:
                    tmp+=1
                elif i>=left and i<mid:
                    cnt+=1
            if tmp>1:
                return mid
            elif cnt>mid-left:
                right=mid-1
            else:
                left=mid+1