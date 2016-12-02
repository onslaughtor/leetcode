'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
'''
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t)==0:
            return ""
        d={}
        for i in t:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        left=0
        right=0
        cnt=0
        ans=(0,len(s))
        
        while right<len(s):
            if s[right] in d:
                d[s[right]]-=1
                if d[s[right]]>=0:
                    cnt+=1
            if cnt==len(t):
                while left<right:
                    if s[left] in d:
                        if d[s[left]]==0:
                            break
                        else:
                            d[s[left]]+=1
                    left+=1
                if right-left<ans[1]-ans[0]:
                    ans=(left,right)
            right+=1
        if cnt<len(t):
            return ''
        else:
            return s[ans[0]:ans[1]+1]

'''
Solution: scan S from left to right until all characters in T has appeared, some may appeared more than once.
    move the left pointer forward until all the charaters appeared exactly once
    that's one window. move the right pointer to find other windows.
Type: Two Pointer
'''