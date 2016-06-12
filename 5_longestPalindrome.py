class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return ''
        resL,resR=0,0
        pali=[([0] * len(s)) for i in range(len(s))]
        for i in range(len(s)):
            pali[i][i]=1
            if i>0 and s[i]==s[i-1]:
                pali[i-1][i]=1
                resL,resR=1,1
        for n in range(3,len(s)+1):
            for i in range(0,len(s)):
                if i+n>len(s):
                    break
                if pali[i+1][i+n-2]and s[i]==s[i+n-1]:
                    pali[i][i+n-1]=1
                    resL,resR=i,i+n-1
        return s[resL:resR+1]


print Solution().longestPalindrome('aaa')