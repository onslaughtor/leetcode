# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.search(root)[0]
        
    def search(self,root):
        max_chain=root.val
        ans=root.val
        tmp=root.val
        if root.left is not None:
            a,b=self.search(root.left)
            ans=max(ans,a)
            if b>0:
                tmp+=b
                max_chain=max(max_chain,root.val+b)
        if root.right is not None:
            a,b=self.search(root.right)
            ans=max(ans,a)
            if b>0:
                tmp+=b
                max_chain=max(max_chain,root.val+b)
        return max(ans,tmp),max_chain
