'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.
Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
'''
# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if root is None:
            self.root=None
            return 
        self.dfs(root,None)
        self.root=root.left

    def dfs(self,node,father):
        if node.left is not None:
            self.dfs(node.left,node)
            node.left=node.left.left
        else:
            node.left=node
        if node.right is not None:
            self.dfs(node.right,father)
            node.right=node.right.left
        else:
            node.right=father
        
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.root is not None

    def next(self):
        """
        :rtype: int
        """
        ans=self.root.val
        self.root=self.root.right
        return ans



'''
Solution: re-define the left and right property while trackback during DFS
        node.left represents the leftest node of the subtree
        node.right represents the next smallest node of the subtree(successor)
Type: Binary Search Tree
'''