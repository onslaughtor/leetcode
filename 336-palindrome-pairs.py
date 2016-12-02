'''
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
'''
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        d={}
        for i in xrange(len(words)):
            d[words[i][::-1]]=i
        ans=[]
        for i in xrange(len(words)):
            w=words[i]
            if len(w)==0:
                for w in d:
                    if w!='' and self.isPalindrome(w):
                        ans.append([i,d[w]])
                        ans.append([d[w],i])
                continue
            for j in xrange(len(w)):
                if w[j:] in d and d[w[j:]]!=i and self.isPalindrome(w[:j]):
                    ans.append([d[w[j:]],i])
                if j+1<len(w) and w[:j+1] in d and d[w[:j+1]]!=i and self.isPalindrome(w[j+1:]):
                    ans.append([i,d[w[:j+1]]])
        return ans
                    
    
    def isPalindrome(self,s):
        i,j=0,len(s)-1
        while i<j and s[i]==s[j]:
            i+=1
            j-=1
        return i>=j