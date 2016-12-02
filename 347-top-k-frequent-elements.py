class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt={}
        for i in nums:
            cnt[i]=cnt.get(i,0)+1
        bucket=[[] for i in xrange(len(nums))]
        for i in cnt:
            bucket[cnt[i]-1].append(i)
        ans=[]
        for i in xrange(len(bucket)-1,-1,-1):
            for x in bucket[i]:
                if len(ans)==k:
                    return ans
                else:
                    ans.append(x)
        return ans
        