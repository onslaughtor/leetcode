'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<3:
            return 0
        right=[0]*len(height)
        for i in range(len(height)-2,-1,-1):
            right[i]=max(right[i+1],height[i+1])

        left=height[0]
        ans=0
        for i in range(1,len(height)):
            if left>height[i] and right[i]>height[i]:
                ans+=min(left,right[i])-height[i]
            else:
                left=max(left,height[i])
        return ans

a=[0,1,0,2,1,0,1,3,2,5,2,1,4]
b=[0,1,0,2,1,0,1,3,2,1,2,1]
print Solution().trap(a)

'''        
Solution: Let left[i] be the highest line left to ith line 
    and right[i] be the height to the right, both are exclusive.
    the area above i is min(left[i],right[i])-height[i], add each area up
Type: DP
'''

 