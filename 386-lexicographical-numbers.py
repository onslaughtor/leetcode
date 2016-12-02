'''
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
'''
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self.ans=[]
        # self.dfs(0,n)
        self.bitmove(n)
        return self.ans
    
    def bitmove(self,n):
        cur=1
        for i in xrange(n):
            self.ans.append(cur)
            if cur*10<=n:
                cur*=10
            else:
                while cur+1>n or cur%10==9:
                    cur/=10
                cur+=1
        return self.ans 
        
    def dfs(self,pre,n):
        for i in xrange(10):
            if pre==0 and i==0:
                continue
            if pre*10+i>n:
                break
            self.ans.append(pre*10+i)
            self.dfs(pre*10+i,n)
 