# Definition for an interval.  
# class Interval(object):  
#     def __init__(self, s=0, e=0):  
#         self.start = s  
#         self.end = e  
import heapq  
  
class Solution(object):  
    def minMeetingRooms(self, intervals):
        heap=[] 
        intervals.sort(cmp=lambda x,y: cmp(x.start, y.start))  
        for i in intervals:  
            if len(heap) == 0 or heap[0] > i.start:  
                heapq.heappush(heap, i.end)  
            else:
                heapq.heapreplace(heap, i.end)    
        return len(heap)