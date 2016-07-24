'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''
# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n=len(points)
        if n<3:
            return n
        ans=0
        for i in xrange(n):
            d=dict()
            cnt=1
            for j in xrange(i+1,n):
                if points[i].x==points[j].x and points[i].y==points[j].y:
                    cnt+=1
                else:
                    if points[i].y== points[j].y:
                        g='*'
                    else:
                        g=1.0*(points[i].x-points[j].x)/(points[i].y-points[j].y)
                    if g not in d:
                        d[g]=1
                    else:
                        d[g]+=1
            ans=max(ans,cnt)
            for g in d:
                ans=max(ans,d[g]+cnt)
        return ans


'''
Solution: points on the same line have the same gradients of some point
Type: Mathematics
'''
