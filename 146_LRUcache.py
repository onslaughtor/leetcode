'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
'''

class Node:
    def __init__(self,key,val,pre,next):
        self.key=key
        self.val=val
        self.pre=pre
        self.next=next

class LRUCache(object):
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.n=capacity
        self.head=None
        self.tail=None
        self.mp={}
        

    def get(self, key):
        """
        :rtype: int
        """
        if self.n>0 and key in self.mp:
            self.tohead(self.mp[key])
            return self.mp[key].val
        else:     
            return -1 
            
    def tohead(self,node):
        if node==self.head:
            return 
        node.pre.next=node.next
        if node==self.tail:
            self.tail=node.pre
        else:
            node.next.pre=node.pre
        node.pre=None
        node.next=self.head
        self.head.pre=node
        self.head=node
        
    def remove(self):
        del self.mp[self.tail.key]
        self.tail=self.tail.pre
        self.tail.next=None
        
    def add(self,key,value):
        node=Node(key,value,None,None)
        self.mp[key]=node
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head.pre=node
            self.head=node
       

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.n<1:
            return 
        if key in self.mp:
            self.mp[key].val=value
            self.tohead(self.mp[key])
        else:
            self.add(key,value)
            if len(self.mp)>self.n:
                self.remove()
                
        