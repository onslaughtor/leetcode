'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=nums[0]
        pos,neg=0,0
        for i in nums:
            if i==0:
                pos,neg=0,0
            elif i>0:
                pos,neg=max(pos*i,i),neg*i
            else:
                pos,neg=neg*i,min(i,pos*i)
            if i==0:
                ans=max(ans,0)
            else:
                if pos>0:
                    ans=max(ans,pos)
                if neg<0:
                    ans=max(neg,ans)
        return ans
                    
                    
                
            