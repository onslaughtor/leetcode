'''
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.
'''

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[i for i in xrange(n+1)]
        dp[-1]=-1

        for i in xrange(n):
            j=0
            while i-j>=0 and i+j<n and s[i-j]==s[i+j]:
                dp[i+j]=min(dp[i+j],dp[i-j-1]+1)
                j+=1
            j=0
            while i-j>=0 and i+1+j<n and s[i-j]==s[i+1+j]:
                dp[i+1+j]=min(dp[i+1+j],dp[i-j-1]+1)
                j+=1
            print dp
        return dp[n-1]
'''
Solution:
    dp[k] means the mininum cuts for the first k characters
    dp[k]=min(dp[j]+1 for any j that s[j:k] is a palindrome), but the nested palindrome check is also O(n), so totally O(n*n) for each k
    but when use kth character as the pivot of the palindrome it belongs to, we can check it while tarversing all 'j'
    and stop the traverse immediately using the monotonicity of palindrome
Type: DP
Inspiration: 
    - we're used to check palindrome from two ends but ignore checking from mid to ends, which has a good property
    - when it comes to the kth elements in DP, it not a MUST to update dp[k] but anyone following it(no afteraffect)
'''
        
