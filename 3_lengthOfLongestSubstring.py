'''
Given a string, find the length of the longest substring without repeating characters.
'''
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


'''
Solution: traverse the string, record the last position of each letter and the position last repeated letter. 
    if the current letter has appeared before, the beginning of the substring ending with current letter is minnum of lastAppear and lastReapt
    update the two kinds of variable and maximum length
Type: Implement
'''