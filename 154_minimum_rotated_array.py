'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.The array may contain duplicates.
'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        ans=nums[0]
        while left<=right:
            mid=(left+right)/2
            if nums[left]==nums[right]:
                left+=1
                right-=1
            elif nums[left]<=nums[mid] and nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid-1
            ans=min(ans,nums[mid])
        return ans

'''
Solution: binary search to find the position of the povit
        solve the tough problem from a simpler version with no duplicate
        add the left==right condition to handle duplicate
Type: Binary Search
Inspiration: when it is not abusolutely monotonic, binary search plus traverse is better than pure traverse
'''