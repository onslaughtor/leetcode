'''
A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.
'''
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n=len(A)
        start=0
        ans=0
        while start<n-1:
            end=start+1
            delta=A[end]-A[start]
            while end<n and A[end]-A[end-1]==delta:
                end+=1
            ans+=(end-start-2)*(end-start-1)/2
            if end==start+1:
                start=end
            else:
                start=end-1
        return ans 