'''
Given a string that contains only digits 0-9 and a target value, 
return all possibilities to add binary operators (not unary) +, -, or * 
between the digits so they evaluate to the target value.
'''
class Solution(object):
    ans={}
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        return self.solve(num,target,1)
        
    def solve(self,num,target,f):
        # print num,target,f
        key=num+'#'+str(target)+'#'+str(f)
        if key in self.ans:
            return self.ans[key]
        else:
            self.ans[key]=[]
        if self.isNumber(num) and int(num)*f==target:
            self.ans[key].append(num)
        for i in xrange(1,len(num)):
            x=num[:i]
            y=num[i:]
            if not self.isNumber(y):
                continue
            for j in self.solve(x,target-int(y)*f,1):
                self.ans[key].append(j+'+'+y)
            for j in self.solve(x,int(y)*f+target,1):
                self.ans[key].append(j+'-'+y)
            for j in self.solve(x,target,int(y)*f):
                self.ans[key].append(j+'*'+y)
        return self.ans[key] 
    
    def isNumber(self,num):
        return len(num)>0 and (len(num)==1 or num[0]!='0')
        