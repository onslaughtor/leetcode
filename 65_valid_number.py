class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        idx=0
        dot=0
        neg=0
        space=0
        num=0
        e=0
        for i in s:
            print i
            if i==' ' and idx==0 and e==0:
                continue
            elif i==' ' and idx>0: 
                space=1
            elif space==1:
                return False
            elif i>='0' and i<='9':
                idx+=1
                num=idx
            elif (i=='-' or i=='+') and idx==0:
                neg=1
                idx+=1
            elif i=='.' and dot==0:
                dot=1
                idx+=1
                if num>0:
                    num=idx
            elif i=='e' and num>0 and e==0:
                idx=0
                num=0
                neg=0
                e=1
                dot=1
            else:
                return False     
        return num==idx and num>0



print Solution().isNumber('0')
print Solution().isNumber(' 0.1 ')
print Solution().isNumber('abc')
print Solution().isNumber('2e10')
print Solution().isNumber('.1')
print Solution().isNumber('1.')
print Solution().isNumber('3e12.5')
print Solution().isNumber('+12e-12')
print Solution().isNumber('+12e1.2')