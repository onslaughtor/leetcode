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