'''
Given a 2D binary matrix filled with 0's and 1's, 
find the largest rectangle containing only 1's and return its area.
'''

class Solution(object):
    # similar to 84.largest_rectangle
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0:
            return 0  
        n=len(matrix)
        m=len(matrix[0])
        height=[0]*(m+1)
        ans=0

        for i in range(n):
            stack=[]
            for j in range(m+1):
                if j==m or matrix[i][j]=='0':
                    height[j]=0
                else:
                    height[j]+=1
                while len(stack)>0 and height[stack[-1]]>=height[j]:
                    idx=stack.pop()
                    if len(stack)==0:
                        ans=max(ans,height[idx]*j)
                    else:
                        ans=max(ans,height[idx]*(j-stack[-1]-1))
                stack.append(j)
        return ans 

print Solution().maximalRectangle([['1','1','0','1'],['1','1','0','1'],['0','1','0','1']])