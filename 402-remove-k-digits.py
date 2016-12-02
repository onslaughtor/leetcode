'''
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
'''
class Solution(object):
    
    def removeKdigits(self, num, k):
        n=len(num)
        ans=[]
        for i in xrange(n):
            while n-i>n-k-len(ans) and len(ans)>0 and ans[-1]>num[i]:
                ans.pop()
            if len(ans)<n-k:
                ans.append(num[i])
        for i in xrange(0,len(ans)):
            if ans[i]!='0':
                break
        if len(ans)==0:
            return '0'
        else:
            return ''.join(ans[i:])
    
    def removeKdigits2(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        pos=[[] for i in xrange(10)]
        ans=[1]*len(num)
        ri=-1
        while k>0:
            if ri+k==len(num)-1:
                for i in xrange(ri+1,len(num)):
                    ans[i]=0
                break
            for i in xrange(10):
                if len(pos[i])>0 and pos[i][-1]<=ri+k+1:
                    break
            ri=pos[i].pop()
            for i in xrange(10):
                while len(pos[i])>0 and pos[i][-1]<ri:
                    ans[pos[i].pop()]=0
                    k-=1
        s=''
        for i in xrange(len(num)):
            if ans[i]==1 and (len(s)>0 or num[i]!='0'):
                s+=num[i]
        if len(s)==0:
            return '0'
        else:
            return s
        
                    
            
            
            