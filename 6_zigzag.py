class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        res=''
        for i in range(numRows):
            idx=i
            while idx<len(s):
                res+=s[idx]
                if i>0 and i<numRows-1 and idx+(numRows-i-1)*2<len(s):
                    res+=s[idx+(numRows-i-1)*2]
                idx+=(numRows-1)*2
        return res

print Solution().convert('PAYPALISHIRING',3)
'''
P   A   H   N
A P L S I I G
Y   I   R
PAHNAPLSIIGYIR
'''