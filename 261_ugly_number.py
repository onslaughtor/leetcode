'''
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note that 1 is typically treated as an ugly number.
'''
from collections import deque

class Solution(object):


    def nthUglyNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    ans=[1]
    index=[0]*3
    for i in xrange(n-1):
        m1,m2,m3=ans[index[0]]*2,ans[index[1]]*3,ans[index[2]]*5
        mm=min(m1,m2,m3)
        if m1==mm:
            index[0]+=1
        if m2==mm:
            index[1]+=1
        if m3==mm:
            index[2]+=1
        ans.append(mm)
    return ans[-1]


    def nthUglyNumber2(self, n):
        """
        :type n: int
        :rtype: int
        """
        st=set([1])
        h2=deque([1])
        h3=deque([1])
        h5=deque([1])
        ans=1
        while n>1:
            x2=h2[0]*2
            x3=h3[0]*3
            x5=h5[0]*5
            if x2<=x3 and x2<=x5:
                ans=x2
                h2.popleft()
            elif x3<=x2 and x3<=x5:
                ans=x3
                h3.popleft()
            else:
                ans=x5
                h5.popleft()
            if ans not in st:
                st.add(ans)
                n-=1
                h2.append(ans)
                h3.append(ans)          
                h5.append(ans)
        return ans 


'''
Solution: the next ugly number must be [2,3,5] multify the previous ugly number
    maitain three queue where the elements have not be multified by x(2,3,5) and orders ascending
    the next one is the minimum of the three top elements which has not appear 
'''