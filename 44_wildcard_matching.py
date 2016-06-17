class Solution(object):
    
    def equal(self,s,p):
        return p=='?' or s==p

    def kmp(self,s,p):
        next=[0]*len(p)
        for i in range(1,len(p)):
            k=i-1
            while k>=0 and next[i]==0:
                # can not swap!
                if self.equal(p[i],p[next[k]]):
                    next[i]=next[k]+1
                else:
                    k=next[k]-1
        i,j=0,0
        while i<len(s):
            if self.equal(s[i],p[j]):
                j+=1
                if j==len(p):
                    return i 
                i+=1
            elif j>0: 
                j=next[j-1]
            else:
                i+=1
   
        return -1


    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p)==0 and len(s)>0:
            return False
        pre=0
        start=0
        for i in range(len(p)):
            if p[i]=='*':
                if i>pre:
                    idx=self.kmp(s[start:],p[pre:i])
                    if idx==-1:
                        return False
                    # to match the head
                    elif pre==0 and idx>i-1:
                        return False
                    else:
                        start+=idx+1
                pre=i+1
        ## to match the tail
        if pre<len(p):
            if pre==0:
                ## entirely same
                return len(s)==len(p) and self.kmp(s,p)>-1
            else:
                ## match the tail
                return start<=len(s)-len(p)+pre and self.kmp(s[len(s)-len(p)+pre:],p[pre:])>-1
        else:
            return True


print Solution().isMatch("aaabaaabaabababbabababaababbabbbbaaaaababbaabbbaab", "*babbbb*aab**b*bb*aa*")
print Solution().isMatch('abb','*a?b')