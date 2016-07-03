class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2)!=len(s3):
            return False
        dp=[[0]*(len(s1)+1) for i in xrange(len(s3)+1)] 
        dp[0][0]=1
        for i in range(1,len(s3)+1):
            for k in range(1,i+1):
                if k<=len(s1) and i-k<=len(s2) and s3[i-1]==s1[k-1]:
                    dp[i][k]+=dp[i-1][k-1]
                if k<=len(s2) and i-k<=len(s1) and s3[i-1]==s2[k-1]:
                    dp[i][i-k]+=dp[i-1][i-k]
            if max(dp[i])==0:
                return False
        return dp[len(s3)][len(s1)]>0


s1 = "aabcc"
s2 = "dbbca"
print Solution().isInterleave(s1,s2,"aadbbcbcac")
print Solution().isInterleave(s1,s2,"aadbbbaccc")
print Solution().isInterleave("ab","bc","bcba")
