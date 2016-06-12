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
    #linked list O(nlogn)
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