from collections import deque
'''
Given an array nums, there is a sliding window of size k which is moving from left to right. 
You can only see the k numbers in the window. return the maximum in each window
'''
from collections import deque 
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue=deque([])
        ans=[]
        for i in range(len(nums)):
            if len(queue)>0 and queue[0]+k-1<i:
                queue.popleft()
            while len(queue)>0 and nums[queue[-1]]<nums[i]:
                queue.pop()
            queue.append(i)
            if i+1>=k:
                ans.append(nums[queue[0]])
        return ans 
    
'''
Solution: maintan a queue that idex ascending and value descending and idex within kth distance
Type: Prioriry Queue
Comment: deque has no method 'popright'
'''