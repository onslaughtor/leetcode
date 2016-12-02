'''
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. 
Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.
Note: n will be less than 15,000.
'''
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack=[]
        for n in nums:
            if len(stack)==0 or stack[-1][0]>n:
                stack.append((n,n))
            elif stack[-1][0]<n:
                left=stack[-1][0]
                while len(stack)>0 and stack[-1][1]<=n:
                    stack.pop()
                if len(stack)>0 and stack[-1][0]<n:
                    return True
                stack.append((left,n))
        return False
                
                    
                              
                