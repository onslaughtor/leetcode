# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res=[]
        flag=0
        for i in intervals:
            if i.end<newInterval.start:
                res.append(i)
            elif i.start>newInterval.end:
                if flag==0:
                    res.append(newInterval)
                    flag=1
                res.append(i)
            else:
                newInterval.start=min(newInterval.start,i.start)
                newInterval.end=max(newInterval.end,i.end)
        if flag==0:
            res.append(newInterval)
        return res

a=[(1,2),(3,5),(6,7),(8,10),(12,16)]
l=[]
for i in a:
    l.append(Interval(i[0],i[1]))

res=Solution().insert(l,Interval(4,9))
for i in res:
    print i.start,i.end
