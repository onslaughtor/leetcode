class Solution(object):
    def buildST(self,nums):
        st=[]
        for i in range(len(nums)):
            st.append([i])
        j=0
        while (1<<(j+1))<=len(nums):
            j+=1
            for i in range(len(nums)):
                st[i].append(st[i][j-1])
                if i+(1<<j)<len(nums) and nums[st[i+(1<<j)][j-1]]>nums[st[i][j-1]]:
                    st[i][j]=st[i+p][j-1]

        return st

    def findMax(self,nums,st,left,right):
        p=0
        while left+(1<<(p+1))-1<right:
            p+=1
        ans=st[left][p] 
        if nums[st[right-(1<<p)+1][p]]>nums[ans]:
            ans=st[right-(1<<p)+1][p]
        return ans 

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return 0
        for i in range(n):
            nums[i]=min(n-1,nums[i]+i)
        # st=self.buildST(nums)
        ans=1
        cur=0
        left=0
        while(nums[cur]<n-1):
            tmp=cur
            for i in range(left,nums[cur]+1):
                if nums[i]>nums[tmp]:
                    tmp=i
            left=nums[cur]+1
            cur=tmp
            ans+=1
        return ans


print Solution().jump([2,1,1,1,1])
        
