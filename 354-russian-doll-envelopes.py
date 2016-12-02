'''
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)
'''
import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n=len(envelopes)
        envelopes.sort(key = lambda x: (x[0],-x[1]))
        last=[]
        for i in xrange(n):
            idx=bisect.bisect_left(last,envelopes[i][1])
            if idx>=len(last):
                last.append(envelopes[i][1])
            else:
                last[idx]=envelopes[i][1]
            left,right=1,len(last)
        return len(last)