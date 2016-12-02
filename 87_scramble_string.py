'''
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
To scramble the string, we may choose any non-leaf node and swap its two children.
Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
'''

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
        if sorted(s1)!=sorted(s2):
            return False
        for i in xrange(1,len(s1)):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            if self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i]):
                return True
        return False
            

print Solution().isScramble_dp('abc','cab')
print Solution().isScramble('great','regat')

'''
Solution: Enumerate the split point and the check isomorphism of the respective left part and right part recursively. 
    Remember to check scramble operation of the node itself, which means the left part of s1 can be isomorphic to either left or right part of s2. 
    use memorization or check the the equality of sorted string to prune.     

    Another solution is DP,

Type: Recursion, DP
'''