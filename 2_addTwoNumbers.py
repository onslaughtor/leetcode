'''
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
        	return l2 
        flag=0
        result=l1 
        while l2 or flag:
        	flag+=l1.val
        	if l2:
        		flag+=l2.val
 	        l1.val=flag%10
 	        flag/=10
 	        if l2:
 	        	l2=l2.next
 	        if (l2 or flag>0) and l1.next is None:
 	        	l1.next=ListNode(0)  
 	        l1=l1.next		
	return result



'''
Solution: traverse l2 and add the number to respective bit of l1.
    define a variable to record whether there's a carry from previous bit
    if l2 plus carry is longer than l1, then extend l1
Type: Implement
'''