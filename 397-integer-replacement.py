
'''
Given a positive integer n and you can do operations as follow:
If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
'''
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        while n>1:
            if n==3:
                ans+=2
                break
            if n&1==0:
                n>>=1
            elif n&2==0:
                n-=1
            else:
                n+=1
            ans+=1
        return ans