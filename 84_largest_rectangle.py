'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.
'''
class Solution(object):
    # build the Sparse Table
    def build_st(self,h):
        k=1
        n=len(h)
        while (1<<k)<n:
            k+=1
        st=[[] for i in range(n)]
        for i in range(n):
            st[i].append(i)
        for j in range(1,k):
            for i in range(n-(1<<j)+1):
                st[i].append(st[i][j-1] if h[st[i][j-1]]<h[st[i+(1<<(j-1))][j-1]] else st[i+(1<<(j-1))][j-1])
        return st
    # area=width*height try by increasing width
    def search(self,st,h,left,right):
        k=0
        while (1<<(k+1))<right-left+1:
            k+=1
        idx=st[left][k] if h[st[left][k]]<h[st[right-(1<<k)+1][k]] else st[right-(1<<k)+1][k]
        ans=h[idx]*(right-left+1)
        if idx!=left:
            ans=max(ans,self.search(st,h,left,idx-1))
        if idx!=right:
            ans=max(ans,self.search(st,h,idx+1,right))
        return ans
   
    # recursion+ST O(nlogn) runtime error
    def largestRectangleArea1(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights)==0:
            return 0
        st=self.build_st(heights)
        return self.search(st,heights,0,len(heights)-1)

    # use stack to record left/right nearest point whose height is less than current,O(n)
    def largestRectangleArea(Self,heights):
        heights.append(0)
        stack=[]
        ans=0
        for i in range(len(heights)):
            while len(stack)>0 and heights[i]<=heights[stack[-1]]:
                idx=stack.pop()
                if len(stack)==0:
                    ans=max(ans,heights[idx]*i)
                else:
                    ans=max(ans,heights[idx]*(i-stack[-1]-1))
            stack.append(i)
        return ans 
        
print Solution().largestRectangleArea([2,1,5,6,2,3,5,4,7,4,3,2])
# print Solution().largestRectangleArea([2,1,5,6,2,3])

'''
Solution: scan the lines and we want to know the area of rectangle whose height is dertermined by this line,
    it is determined by the position of the first shorter line to the left and right.
    use a stack to record the lines in increasing order, each time when we want to put a new line to the stack,
    while the top line is equal to higher than it, we keep poping the top element,
    the current line is the first shorter line left to the popped line and the previous line in the stack is the first shorter line to its left
Type: Priority Queue
'''