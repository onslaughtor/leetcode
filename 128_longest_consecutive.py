class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st=set([])
        for i in nums:
            st.add(i)
        ans=0
        for i in nums:
            if i in st:
                st.remove(i)
                k=i+1 
                l=1
                while k in st:
                    st.remove(k)
                    k+=1
                    l+=1
                k=i-1
                while k in st:
                    st.remove(k)
                    k-=1
                    l+=1
                ans=max(ans,l)
        return ans