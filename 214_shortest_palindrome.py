'''
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. 
Find and return the shortest palindrome you can find by performing this transformation.
'''
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t=s+'#'+s[::-1]
        nxt=[-1]*len(t)
        for i in xrange(1,len(t)):
            j=nxt[i-1]
            while j>=0 and t[i]!=t[j+1]:
                j=nxt[j]
            if t[i]==t[j+1]:
                nxt[i]=j+1
        print t
        print nxt
        return s[:nxt[-1]:-1]+s

print Solution().shortestPalindrome('aabbaa')

'''
Solution:
Type: KMP
Inspiration: palindrome related algorithms are often strange and creative 
'''