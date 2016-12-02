'''
'Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
'''
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min1,min2=None,None
        for i in nums:
            if min1 is None or i<min1:
                min1=i
            elif i>min1 and (min2 is None or i<min2):
                min2=i
            elif min2 is not None and i>min2:
                return True
        return False