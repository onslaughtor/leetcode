'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
You are given a target value to search.no duplicate exists in the array.
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)/2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[left]:
                if target>=nums[left] and target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if target>nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1 
        return -1

print Solution().search([3,2],2)


'''
Solution: binary search to locate the pivot and find the target
    if nums[mid]>=nums[left], the the pivot must be in the right, 
        compare target with the left part(because it's ascending) to determine its position
    otherwise the pivot must be in the left and compare target with the right part
Type: Binary Search
Inpiration: to use the binary search ,we have to find the monotonicity even if it's not perfect
'''