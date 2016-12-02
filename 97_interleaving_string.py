'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
'''
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
        dp=[[0]*(len(s2)+1) for i in xrange(len(s1)+1)] 
        dp[0][0]=1
        for i in xrange(0,len(s1)+1):
            for j in xrange(0,len(s2)+1):
                if (i>0 and s1[i-1]==s3[i+j-1] and dp[i-1][j]==1) or (j>0 and s2[j-1]==s3[i+j-1] and dp[i][j-1]==1):
                    dp[i][j]=1
        return dp[-1][-1]>0
                


s1 = "aabcc"
s2 = "dbbca"
print Solution().isInterleave(s1,s2,"aadbbcbcac")
print Solution().isInterleave(s1,s2,"aadbbbaccc")
print Solution().isInterleave("ab","bc","bcba")
'''
Solution: dp[i][j] means whether the first i+j letters in s3 can be interleft by the fisrt i letters in s1 and first j letters in j.
    dp[i][j]=1 when dp[i-1][j]=1 and s1[i]=s3[i+j] or s2[j]=s3[i+j] and dp[i][j-1]=1.
Type: DP
'''