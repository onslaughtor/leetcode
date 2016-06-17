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