'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        tmp=self.dfs(root)
        return max(tmp,root.val)
        
    def dfs(self,root):
        nval=0
        if root.left is not None:
            tmp=self.dfs(root.left)
            root.val+=tmp
            nval+=max(tmp,root.left.val)
        if root.right is not None:
            tmp=self.dfs(root.right)
            root.val+=tmp
            nval+=max(tmp,root.right.val)
        return nval