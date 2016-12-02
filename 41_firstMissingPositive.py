'''
Given an unsorted integer array, find the first missing positive integer.
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while i<len(nums):
            if nums[i]>0 and nums[i]<=len(nums) and nums[i]!=i+1 and nums[i]!=nums[nums[i]-1]:
                tmp=nums[i]
                nums[i]=nums[tmp-1]
                nums[tmp-1]=tmp
            else:
                i+=1
        ans=len(nums)+1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                ans=i+1
                break
        return ans

a=[2,2,2,2,2]
print Solution().firstMissingPositive(a)

'''
Solution: the missing Positive must between 1 to n(the length of the array).
    traverse the array and put the ith element to position x where arr[i]=x and x in [1,n] by swaping
    After traverse, find the first i that a[i]!=i
Type：Implement
'''