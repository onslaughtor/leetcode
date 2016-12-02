'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.
'''
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n=len(matrix)
        queue=[]
        for i in xrange(n):
            heapq.heappush(queue,(matrix[0][i],0,i))
        while len(queue)>0:
            ans,x,y=queue[0]
            if k==1:
                return ans
            else:
                k-=1
            if x+1<n:
                heapq.heapreplace(queue,(matrix[x+1][y],x+1,y))
            else:
                heapq.heappop(queue)
        return ans
            
        