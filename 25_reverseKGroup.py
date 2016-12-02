'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k<2:
            return head
        superhead=ListNode(0)
        superhead.next=head
        lastTail=superhead
        start,cur=head,head 
        cnt=0
        while cur is not None:
            cnt+=1
            if cnt<k:
               cur=cur.next
               continue
            nextStart=cur.next
            tmp=start
            nextcur=cur.next
            while tmp is not nextcur:
                nexttmp=tmp.next
                tmp.next=nextStart
                nextStart=tmp
                tmp=nexttmp
            lastTail.next=cur

            lastTail=start
            start=nextcur
            cnt=0
            cur=nextcur
        print self.debug(superhead.next)
        return superhead.next

    def debug(self,head):
        res=""
        while head is not None:
            res+=str(head.val)+"->"
            head=head.next
        return res

def generateList(l):
    head=ListNode(-1)
    tmp=head
    for i in l:
        a=ListNode(i)
        tmp.next=a 
        tmp=tmp.next
    return head.next

Solution().reverseKGroup(generateList([1,2,3,4,5]),2)
'''
Solution: record the tail of last group and the head of the next group while traverse each group from right to left, 
hang it to the tail of the last tail one by one and hang next start to the current tail. 
use a superhead and supertail to reduce boundary check
Type: LinkedList
'''