'''
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        pre={}
        ans=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                if len(stack)>0:
                    idx=stack.pop()
                    if idx-1 in pre:
                        pre[i]=pre[idx-1]
                    else:
                        pre[i]=idx
                    if i-pre[i]+1>ans:
                        ans=i-pre[i]+1
        return ans

print Solution().longestValidParentheses(')()(()(())()((()')


'''
Solution: use a stack to record the position of unmatched '('.
    dp[i] represent the left end of the longest valid sequence that ends at i if i is ')'
    let x be the position of the matched '(', dp[i]=dp[x-1] when x-1 is a ')' otherwise x
    the answer is the maximum of i-dp[i]+1
Type: DP
''' 