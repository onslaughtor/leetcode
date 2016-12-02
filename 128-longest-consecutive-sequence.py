'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st=set(nums)
        ans=0
        while len(st)>0:
            for i in st:
                n=i
                break
            st.remove(n)
            tmp=1
            m=n+1
            while m in st:
                st.remove(m)
                tmp+=1
                m+=1
            m=n-1
            while m in st:
                st.remove(m)
                tmp+=1
                m-=1
            ans=max(ans,tmp)
        return ans 
                