'''
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
'''
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n=len(stones)
        d={}
        for i in xrange(n):
            d[stones[i]]=i
        next=[set([]) for i in xrange(n)]
        next[0]=set([1])
        for i in xrange(n):
            for j in next[i]:
                pos=stones[i]+j
                if pos==stones[-1]:
                    return True
                if pos in d and d[pos]>i:
                    self.put(pos,next[d[pos]],j)
        return False
                    
    def put(self,pos,st,x):
        if x>1:
            st.add(x-1)
        if x>0:
            st.add(x)
        st.add(x+1)
