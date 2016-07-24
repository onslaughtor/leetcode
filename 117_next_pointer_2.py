# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        first=None
        pre=None
        while root is not None:
            if root.left is not None:
                if first is None:
                    first=root.left
                if pre is not None:
                    pre.next=root.left
                pre=root.left
            if root.right is not None:
                if first is None:
                    first=root.right
                if pre is not None:
                    pre.next=root.right
                pre=root.right
            if root.next is not None:
                root=root.next
            else:
                root=first
                first=None
                pre=None
