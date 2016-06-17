# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n=len(lists)
        if n==0:
            return []
        if n==1:
            return lists[0]
        if n==2:
            return self.merge(lists[0],lists[1])
        return self.merge(self.mergeKLists(lists[0:n/2]),self.mergeKLists(lists[n/2:n]))


    def merge(self,a,b):
        head=ListNode(-1)
        tmp=head
        while a is not None or b is not None:
            if a is None:
                tmp.next=b
                b=b.next 
            elif b is None:
                tmp.next=a
                a=a.next
            elif a.val<b.val:
                tmp.next=a 
                a=a.next
            else:
                tmp.next=b
                b=b.next
            print tmp.val
            tmp=tmp.next
        return head.next
