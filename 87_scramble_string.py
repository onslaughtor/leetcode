class Solution(object):

    def isScramble_dp(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1==s2:
            return True
        if len(s1)!=len(s2):
            return False
        n=len(s1)
        dp=[[[0]*n for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if s1[i]==s2[j]:
                    dp[i][j][0]=1
        for k in range(1,n):
            for i in range(n-k):
                for j in range(n-k):
                    for t in range(k):
                        if dp[i][j][t]==1 and dp[i+t+1][j+t+1][k-t-1]==1:
                            dp[i][j][k]=1
                            break
                        if dp[i][j+k-t][t]==1 and dp[i+t+1][j][k-t-1]==1:
                            dp[i][j][k]=1
                            break
        return dp[0][0][n-1]==1

    # recursion O(n^n),but runtime=50ms with pruning, much faster than DP(runtime=500ms)
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1==s2:
            return True
        if len(s1)!=len(s2):
            return False
        d={}
        cnt=0
        for i in range(len(s1)-1):
            d[s1[i]]=1 if s1[i] not in d else d[s1[i]]+1
            if d[s1[i]]<=0:
                cnt+=1
            d[s2[i]]=-1 if s2[i] not in d else d[s2[i]]-1
            if d[s2[i]]>=0:
                cnt+=1
            if cnt==i+1 and self.isScramble(s1[i+1:],s2[i+1:]) and self.isScramble(s1[:i+1],s2[:i+1]):
                return True
        d={}
        cnt=0
        for i in range(len(s1)-1):
            d[s1[i]]=1 if s1[i]  not in d else d[s1[i]]+1
            if d[s1[i]]<=0:
                cnt+=1
            d[s2[-i-1]]=-1 if s2[-i-1] not in d else d[s2[-i-1]]-1
            if d[s2[-i-1]]>=0:
                cnt+=1
            if cnt==i+1 and self.isScramble(s1[i+1:],s2[:len(s2)-i-1]) and self.isScramble(s1[:i+1],s2[len(s2)-i-1:]):
                return True
        return False

print Solution().isScramble_dp('abc','cab')
print Solution().isScramble('great','regat')