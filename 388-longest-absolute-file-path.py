'''
Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
'''
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack=[]
        ans=0
        for line in input.split('\n'):
            lev=line.count('\t')
            while lev<len(stack):
                stack.pop()
            stack.append(len(line)-lev)    
            if len(stack)>1:
                stack[-1]+=stack[-2]+1
            if '.' in line and stack[-1]>ans:
                ans=stack[-1]
        return ans