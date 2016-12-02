'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
'''
from operator import itemgetter

class Node:
    def __init__(self,index,l,r):
        self.index=index
        self.left=l
        self.right=r
        if l is not None:
            l.right=self
        if r is not None:
            r.left=self

    def remove(self):
        self.left.right=self.right
        self.right.left=self.left

class Solution(object):
    #linked list Solution O(nlogn)
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        queue=[]
        head=Node(-1,None,None)
        tail=Node(len(height),head,None)
        tmp=head
        for i in range(len(height)):
            n=Node(i,tmp,tail)
            queue.append((i,height[i],n))
            tmp=n 
        queue.sort(key=itemgetter(1))
        maxArea=0
        for t in queue:
            t[2].remove()
            if head.right==tail:
                break
            maxArea=max(maxArea,max(abs(head.right.index-t[0]),abs(tail.left.index-t[0]))*t[1])
           # print t[0],t[1],head.right.index,tail.left.index   
        return maxArea
    # two pointer solution O(n)
    def maxArea(self, height):
        i,j=0,len(height)-1
        maxArea=0
        while i<j:
            maxArea=max(maxArea,(j-i)*min(height[i],height[j]))
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return maxArea        

h=[2,5,3,7,6]
print Solution().maxArea(h) 

'''
Solution#1: sort the line by height then traverse, the area is the distance to the leftest or rightest higher line multify the height of itself
    use a double-linked list to reach the leftest and rightest position
Solution#2:Begin from the two ends, say the current area is W*H, 
    to make it bigger, we must reduce W and improve H, 
    each time desert the shorter line and shrink the segment until two ends meet.vice versa
'''