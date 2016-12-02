'''
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.
'''
import bisect
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        s=[0]
        tmp=0
        ans=0
        for i in nums:
            tmp+=i
            ans+=bisect.bisect_right(s,tmp-lower)-bisect.bisect_left(s,tmp-upper)
            bisect.insort(s,tmp)
        return ans
