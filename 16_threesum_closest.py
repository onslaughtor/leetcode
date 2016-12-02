'''
Given an array S of n integers, 
find three integers in S such that the sum is closest to a given number, target.
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        twoSum=[]
        twoSet=set();
        res=nums[0]+nums[1]+nums[2]
        for j in range(1,len(nums)-1):
            for i in range(0,j):
                s=nums[i]+nums[j]
                if s not in twoSet:
                    twoSum.append(s)
                    twoSet.add(s)
            twoSum.sort()
            tmp=self.search(twoSum,target-nums[j+1])
            if abs(tmp+nums[j+1]-target)<abs(res-target):
                res=tmp+nums[j+1]
            if res==target:
                return res
        return res
        
    def search(self,sum,target):
        left,right=0,len(sum)-1
        mid=(left+right)/2
        while left<=right and sum[mid]!=target:
            mid=(left+right)/2
            if sum[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return sum[mid]         

S = [-1,2,-4,1,6]
#S=[0,0,0]
print Solution().threeSumClosest(S,1)

'''
Solution: traverse the array, compute the two-sum value of the previous nums,
    use binary search to find two-sum that is closet to target-current num
Type: Binary Search
'''