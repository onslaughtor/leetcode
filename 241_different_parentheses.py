'''
Given a string of numbers and operators, 
return all possible results from computing all the different possible ways to group numbers and operators. 
The valid operators are +, - and *.
eg. "2-1-1"[0, 2]   "2*3-4*5" [-34, -14, -10, -10, 10]
'''

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        self.operator=set(['+','-','*'])
        self.ans={}
        self.solve(input)
        return self.ans[input]
        
    def solve(self,num):
        if num in self.ans:
            return 
        self.ans[num]=[]
        isNum=True
        for i in xrange(len(num)):
            if num[i] in self.operator:
                isNum=False
                left=num[:i]
                right=num[i+1:]
                self.solve(left)
                self.solve(right)
                for x in self.ans[left]:
                    for y in self.ans[right]:
                        if num[i]=='+':
                            self.ans[num].append(x+y)
                        elif num[i]=='-':
                            self.ans[num].append(x-y)
                        else:
                            self.ans[num].append(x*y)
        if isNum:
            self.ans[num].append(int(num))
        