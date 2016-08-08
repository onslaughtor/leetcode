'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
'''
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ans=""
        if numerator*denominator<0:
            ans+='-'
        numerator=abs(numerator)
        denominator=abs(denominator)
        ans+=str(numerator/denominator)
        numerator%=denominator
        if numerator>0:
            ans+="."
            numerator=(numerator%denominator)*10
        d=dict()
        while numerator>0:
            while True:
                if numerator in d:
                    idx=d[numerator]
                    return ans[:idx]+'('+ans[idx:]+')'
                else:
                    d[numerator]=len(ans)
                if numerator<denominator:
                    numerator*=10
                    ans+='0'
                else:
                    break
            ans+=str(numerator/denominator)
            numerator=(numerator%denominator)*10
        return ans
            
        
            
print Solution().fractionToDecimal(11,53)
'''
Solution: 
    to find the pattern by example 40/19
    when the numerator repeat, the repeating part ends
    using map to record the position 
Type: Mathematics
'''