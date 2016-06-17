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
        
            

 