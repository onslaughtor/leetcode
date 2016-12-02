'''
 '.' Matches any single character.
 '*' Matches zero or more of the preceding element.
 The matching should cover the entire input string (not partial).
'''
class Solution(object):

    def equal(self,s,p):
        return p=='.' or s==p

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
         """
        match=set([-1]) # matched position set of the previous unit
        for i in range(len(p)):
            if p[i]=='*':
                continue
            tmp=set([])# matched position set of the current unit
            # '*' and its previous character is one unit
            if i+1<len(p) and p[i+1]=='*':
                for j in match:
                    tmp.add(j)
                    index=j+1
                    while index<len(s) and index not in match and self.equal(s[index],p[i]):
                        tmp.add(index)
                        index+=1
            else:
                for j in match:
                    if j+1<len(s) and self.equal(s[j+1],p[i]):
                        tmp.add(j+1)
            print match,tmp
            match=tmp           
        return len(s)-1 in match    

print Solution().isMatch('aaa','ab*a.')

'''
Solution: traverse the pattern string and use a set to record which position of the input string has been matched
if the letter is asterisk('*'), pass
if the next letter is '*', traverse the matched position and extend each position until mismatch
otherwise, traverse the matched position and  compare weather the next position is matched to the current letter
if the last position of the input string in the match set, it's a perfect match
'''