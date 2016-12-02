'''
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.
'''
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prepre,pre,cnt=None,None,0
        for i in nums:
            if pre==None:
                pre=i
                cnt+=1
                continue  
            if prepre==None:
                if pre!=i:
                    prepre=pre
                    pre=i
                    cnt+=1
                continue
            if i>=pre and pre>prepre:
                pre=i
            elif i<=pre and pre<prepre:
                pre=i
            else:
                prepre=pre
                pre=i
                cnt+=1
        return cnt
                