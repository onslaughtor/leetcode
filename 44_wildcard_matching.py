'''
Implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
'''

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


    def isMatch2(self, s, p):
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

    def isMatch3(self,s,p):
        dp=[[0]*(len(s)+1) for i in xrange(2)]
        dp[0][0]=1
        x=0
        flag=1
        for i in xrange(1,len(p)+1):
            x^=1
            if p[i-1]!='*':
                flag=0
            dp[x][0]=flag
            for j in xrange(1,len(s)+1):
                if (p[i-1]==s[j-1] or p[i-1]=='?') and dp[x^1][j-1]==1:
                    dp[x][j]=1
                elif p[i-1]=='*':
                    dp[x][j]=(dp[x^1][j]|dp[x][j-1])
                else:
                    dp[x][j]=0
        return dp[x][-1]==1

    def isMatch(self,s,p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i=0
        j=0
        star=-1
        head=0
        while i<len(s):
            if j<len(p) and s[i]==p[j] or p[j]=='?':
                i+=1
                j+=1
            elif j<len(p) and p[j]=='*':
                star=j
                head=i
                j+=1
            elif star>-1:
                j=star+1
                head+=1
                i=head
            else:
                return False
        
        while j<len(p) and p[j]=='*':
            j+=1
        return j==len(p)






print Solution().isMatch("aaabaaabaabababbabababaababbabbbbaaaaababbaabbbaab", "*babbbb*aab**b*bb*aa*")
print Solution().isMatch('abb','*a?b')

'''
Solution: a star in pattern matches all the following sequence, so we can record the matched position of last star 
    and try to match the pattern with all the subsequence after this position until meet another star or entirely matched.   
    A faster way is to use KMP to find the first matched pattern until next star.   

    DP is a more straightforward solution but got TLE.
    let dp[i][j] represent whether first i letters in pattern matched first j letters in string,
    dp[i][j]=dp[i-1][j-1] when pattern[i] matches string[j] and dp[i][j]=dp[i][j-1] | p[i-1][j] if pattern[i] is '\*' otherwise 0. 
    A rolling array to can reduce the memory complexity to O(n).

Type: Implement
'''