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
       