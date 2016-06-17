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

