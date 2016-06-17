import sys

class BitOperation:
    def add(self,x,y):
        # if y:
        #     return self.add(x^y,(x&y)<<1)
        # else:
        #     return x
        i=0
        x=int(x)
        y=int(y)
        while y<>0 and i<100:
            x,y=x^y,(x&y)<<1
            i+=1
        return x

    def subtract(self,x,y):
        print self.add(~y,1)
        # return self.add(x,self.add(~y,1))
    
    def multiply(self,x,y):
        ans=04
        sign=0
        if x<0:
            sign=~sign
            x=self.add(~x,1)
        if y<0:
            sign=~sign
            y=self.add(~y,1)
        while y:
            if y&1:
                ans=self.add(ans,x)
            y=y>>1
            x=x<<1
        if sign:
            return self.add(~ans,1)
        else:
            return ans

    def printBit(self,x):
        res=''
        while x:
            res=str(x&1)+res
            x=x>>1
        print res


print BitOperation().add(14,-11)
# print BitOperation().subtract(14,-11)
# print BitOperation().multiply(3,-4)