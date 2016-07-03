# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        pre=None
        cur=root
        f1=None
        f2=None
        while cur is not None:
            if cur.left is None:
                pre,cur,f1,f2=self.update(pre,cur,f1,f2)
            else:
                tmp=cur.left
                while tmp.right is not None and tmp.right!=cur:
                    tmp=tmp.right
                if tmp.right is None:
                    tmp.right=cur
                    cur=cur.left
                else:
                    tmp.right=None
                    pre,cur,f1,f2=self.update(pre,cur,f1,f2)

        if f1 is not None and f2 is not None:
            f1.val,f2.val=f2.val,f1.val

    def update(self,pre,cur,f1,f2):
        if pre is not None and cur.val<pre.val:
            if f1 is None:
                f1=pre 
            f2=cur
        return cur,cur.right,f1,f2

    def buildTree(self,nums):
        root=TreeNode(nums[0])
        for i in range(1,len(nums)):
            tmp=root
            while tmp is not None:
                if tmp.val>nums[i]:
                    if tmp.left is None:
                        tmp.left=TreeNode(nums[i])
                        break
                    else:
                        tmp=tmp.left
                else:
                    if tmp.right is None:
                        tmp.right=TreeNode(nums[i])
                        break
                    else:
                        tmp=tmp.right
        return root

root=Solution().buildTree([3,5,8,1,4,2,7,6])
Solution().recoverTree(root)

#Reference: http://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html