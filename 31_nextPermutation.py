'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return
        cur=len(nums)-2
        while cur>=0 and nums[cur]>=nums[cur+1]:
            cur-=1
        if cur>=0:
            tmp=nums[cur+1:]
            flag=0
            for i in range(1,len(nums)-cur):
                nums[cur+i]=tmp[-i]
                if nums[cur+i]>nums[cur] and flag==0:
                    nums[cur],nums[cur+i]=nums[cur+i],nums[cur]
                    flag=1
        else:
            nums.reverse()
        
a=[4,1,5,3,1]
Solution().nextPermutation(a)
print a

'''
Solution: traverse from right to left to find the first ascending pair
    reverse the right part(descending sequence) 
    swap the last one on the left with the smallest bigger one on the right
Type: Implement
'''