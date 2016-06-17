class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        global nums
        nums=[]
        candidates.sort()
        for i in range(len(candidates)):
            if i==0 or candidates[i]>candidates[i-1]:
                nums.append(candidates[i])
        return self.work(0,target)
        
    def work(self,idx,target):
        res=[]
        if target<0:
            return res
        for i in range(idx,len(nums)):
            if nums[i]==target:
                res.append([nums[i]])
                break
            tmp=self.work(i,target-nums[i])
            for l in tmp:
                res.append([nums[i]]+l)
        return res


print Solution().combinationSum([2,3,6,7],7)