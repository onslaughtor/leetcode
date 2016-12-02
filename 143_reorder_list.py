# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        # find the middle
        mid=head
        tmp=head.next
        while tmp is not None and tmp.next is not None:
            tmp=tmp.next.next
            mid=mid.next
        
        # reverse the right part
        cur=mid.next
        pre=mid
        mid.next=None
        while cur is not None:
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
            
        # merge to list
        while head is not None and pre is not None:
            # print head.val,pre.val
            tmpHead=head.next
            tmpPre=pre.next
            head.next=pre
            pre.next=tmpHead
            head=tmpHead
            pre=tmpPre
    