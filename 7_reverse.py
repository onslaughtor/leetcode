class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """ 
        res=0
        flag=1 
        if x<0:
            x*=-1
            flag=-1
        while x>0:
            res=res*10+x%10
            x/=10
        return res*flag


print Solution().reverse(-57312)