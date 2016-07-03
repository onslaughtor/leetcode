# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)==0:
            return []
        intervals.sort(cmp=lambda x,y:cmp(x.start,y.start))
        start=intervals[0].start
        end=intervals[0].end
        res=[]
        for i in range(len(intervals)):
            if intervals[i].start>end:
                res.append(Interval(start,end))
                start=intervals[i].start
                end=intervals[i].end
            else:
                end=max(end,inntervals[i].end)
        res.append(Interval(start,end))
        return res

a=[(1,3),(2,6),(15,18),(8,10)]
l=[]
for i in a:
    l.append(Interval(i[0],i[1]))

res=Solution().merge(l)
for i in res:
    print i.start,i.end
