'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
'''
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bits={}
        for i in xrange(len(words)):
            tmp=0
            for j in words[i]:
                tmp|=1<<(ord(j)-97)
            if tmp not in bits or len(words[i])>bits[tmp]:
                bits[tmp]=len(words[i])
        ans=0
        for i in bits:
            for j in bits:
                if j&i==0:
                    ans=max(ans,bits[i]*bits[j])
        return ans
                    
        