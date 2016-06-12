class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        twoSum=dict()
        res=[]
        threeSum=set()
        for j in range(1,len(nums)-1):
            for i in range(0,j):
                s=nums[i]+nums[j]
                if s not in twoSum:
                    twoSum[s]=set()
                twoSum[s].add((nums[i],nums[j]))

            if -1*nums[j+1] not in twoSum or (nums[j+1]==nums[j] and nums[j]==nums[j-1] and nums[j]<>0):
                continue
            for t in twoSum[-1*nums[j+1]]:  
                threeSum.add((t[0],t[1],nums[j+1]))   
        for t in threeSum:        
            res.append([t[0],t[1],t[2]])
        return res

S = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
#S = [0,0,0]
print Solution().threeSum(S)