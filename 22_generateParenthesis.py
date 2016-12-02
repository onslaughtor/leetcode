'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.work('',n,n)

    def work(self,s,left,right):
        res=[]
        if left==0 and right==0:
            res.append(s)
        if left>0:
            res+=self.work(s+'(',left-1,right)
        if right>0 and right>left:
            res+=self.work(s+')',left,right-1)
        return res


print Solution().generateParenthesis(3)

'''
Solution: at each position ,when there is less ')' than '(' in the previous result, then we can add a ')'; 
    when the number of '(' is less than n, then '(' can be added. 
    solve the next position recursively
Type: Recursion
'''