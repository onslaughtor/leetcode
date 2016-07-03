import random 
import time 
class Solution(object):
    def add(self,a,b,p,bit):
        val=0
        i=0
        while val>0 or i<len(a):
            while len(b)<=i+bit:
                b.append('0')
            val+=int(b[i+bit])
            if i<len(a):
                val+=int(a[i])*p
            b[i+bit]=str(val%10)
            val/=10
            i+=1
    
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a=list(num1)[::-1]
        b=list(num2)[::-1]
        ans=['0']
        for i in range(0,len(b)):
            if int(b[i])>0:
                self.add(a,ans,int(b[i]),int(i))
        while len(ans)>1 and ans[-1]=='0':
            ans.pop()
        return ''.join(ans[::-1])


num1,num2='0','5010'
# for i in range(100):
#     num1+=str(int(random.random()*1000000))
#     num2+=str(int(random.random()*1000000))
start = time.time()
print Solution().multiply(num1,num2)
print time.time()-start 
print int(num1)*int(num2)