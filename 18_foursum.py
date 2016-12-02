'''
Given an array S of n integers, 
are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        targetSet=set()
        nums.sort()
        twoSum=dict()
        for j in range(len(nums)-2):
            for i in range(0,j):
                s=nums[i]+nums[j]
                if s not in twoSum:
                    twoSum[s]=set()
                twoSum[s].add((nums[i],nums[j]))

            for k in range(j+2,len(nums)):
                s=target-nums[j+1]-nums[k] 
                if s in twoSum:
                    for t in twoSum[s]:
                        targetSet.add((t[0],t[1],nums[j+1],nums[k]))
        res=[]
        for t in targetSet:
            res.append([t[0],t[1],t[2],t[3]])
        return res

S = [1,0,-1,0,-2,2]
print Solution().fourSum(S,0)

'''
Solution: traverse the array, compute the two-sum set of the previous nums, 
    then traverse the following nums to check whether target-current-following in the two-sum set
    sort the array firstly to avoid repeated results
'''