class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastAppear={}
        maxL=0
        lastRepeat=-1
        for i in range(len(s)):
        	l=i-lastRepeat
        	if s[i] in lastAppear:
        		if lastAppear[s[i]]>lastRepeat:
        			l=i-lastAppear[s[i]]
				lastRepeat=max(lastRepeat,lastAppear[s[i]])	
        	lastAppear[s[i]]=i       	
        	maxL=max(maxL,l)
    return maxL

print Solution().lengthOfLongestSubstring('pwwkew')
