class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp=[[0]*len(s) for i in range(len(t))]
        head=-1
        cnt=1
        for i in xrange(0,len(t)):
            tmp=len(s)
            for j in xrange(head+1,len(s)):
                if t[i]==s[j]:
                    dp[i][j]=cnt
                    if tmp==len(s):
                        tmp=j 
                if i>0:
                    cnt+=dp[i-1][j]
            haed=tmp
            cnt=0
        ans=0
        for i in xrange(len(s)):
            ans+=dp[-1][i]
        return ans


print Solution().numDistinct('b','b')
print Solution().numDistinct('rabbbit','rabit')