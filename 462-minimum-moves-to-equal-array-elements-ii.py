'''
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.
'''
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        lsum,rsum=0,sum(nums)
        l,r=0,len(nums)
        ans=-1
        for i in nums:
            r-=1
            rsum-=i
            tmp=l*i-lsum+rsum-r*i
            if ans==-1 or tmp<ans:
                ans=tmp
            l+=1
            lsum+=i
        return ans