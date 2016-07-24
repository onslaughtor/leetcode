'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Note: Do not modify the linked list. solve it without using extra space
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        fast=head.next 
        slow=head
        while fast is not None:
            if slow==fast:
                slow=head
                fast=fast.next
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
            slow=slow.next
            fast=fast.next
            if fast is not None:
                fast=fast.next
        return None

'''
Solution:
    X=length before the circle,Y=length of the circle,K=distance from the start of the circle to the met point
    when two pointers met: X+mY+K=2(X+nY+k)->(m-2n)Y=X+K
    additional X step from the met point is the start of the circle
type: LinkedList
Inspiration: creative combination of mathmetics and programming 
'''
