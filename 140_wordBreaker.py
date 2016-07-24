'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """

        ans=[[] for i in xrange(len(s))]
        for i in xrange(len(s)):
            if i==0 or len(ans[i-1])>0:
                for j in xrange(i,len(s)):
                    if s[i:j+1] in wordDict:
                        ans[j].append(i)
        return self.find(ans,len(s)-1,s)

    def find(self,ans,x,s):
        if x<0:
            return [""]
        res=[]
        for i in ans[x]:
            tmp=self.find(ans,i-1,s)
            for l in tmp:
                if l=="":
                    res.append(s[i:x+1])
                else:
                    res.append(l+" "+s[i:x+1])
        return res 


'''
Solution:
    update from left to right, record every matched index
    recursion from right to left to find all solutions
    if we record ans[i].append(j), the recursion would not work because of too many redundant information besides the answer
type: DP
Inspiration: 
'''

