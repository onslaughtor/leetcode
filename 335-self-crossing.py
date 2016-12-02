'''
You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.
'''

class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        for i in xrange(3,len(x)):
            if i>2 and x[i]>=x[i-2] and x[i-1]<=x[i-3]:
                return True
            elif i>3 and x[i-1]==x[i-3] and x[i]+x[i-4]>=x[i-2]:
                return True
            elif i>4 and x[i-5]+x[i-1]>=x[i-3]  and x[i-1]<=x[i-3] and x[i]+x[i-4]>=x[i-2] and x[i-2]>=x[i-4]:
                return True
        return False