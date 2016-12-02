'''
Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3"
'''

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder=='#' or preorder=='':
            return True
        nodes=preorder.split(',')
        stack=[]
        first=1
        for i in nodes:
            if first==0 and len(stack)==0:
                return False
            if first==1 and i=='#':
                return False
            if i=='#':
                if stack[-1][0]==0:
                    stack[-1][0]=1
                elif stack[-1][1]==0:
                    stack[-1][1]=1
                else:
                    return False
            else:
                stack.append([0,0])
                
            while stack[-1][1]==1:
                stack.pop()
                if len(stack)==0:
                    break
                if stack[-1][0]==0:
                    stack[-1][0]=1
                elif stack[-1][1]==0:
                    stack[-1][1]=1
                else:
                    return False
            first=0
        return len(stack)==0
                
                
                
        
        