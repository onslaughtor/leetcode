'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
'''

class LinkedNode:

    def __init__(self,key,val):
        self.pre=None
        self.nxt=None
        self.key=key
        self.val=val

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.d=dict()
        self.head=None
        self.tail=None

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.d:
            self.visit(key)
            return self.d[key].val
        else:
            return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.d:
            tmp=self.head
            self.head=LinkedNode(key,value)
            if tmp is None:
                self.tail=self.head
            else:
                self.head.nxt=tmp
                tmp.pre=self.head
            self.d[key]=self.head
            if self.capacity==0:
                del self.d[self.tail.key]
                self.tail=self.tail.pre
                self.tail.nxt=None
            else:
                self.capacity-=1
        else:
            self.d[key].val=value
            self.visit(key)
        

    def visit(self,key):
        tmp=self.d[key]
        if tmp!=self.head:
            tmp.pre.nxt=tmp.nxt
            if tmp==self.tail:
                self.tail=tmp.pre
            else:
                tmp.nxt.pre=tmp.pre

            self.head.pre=tmp
            tmp.pre=None
            tmp.nxt=self.head
            self.head=tmp


cache=LRUCache(2)
cache.set(2,1)
cache.set(1,1)
print cache.get(2)
cache.set(4,1)
print cache.get(1)
print cache.get(2)

'''
Solution: use doubly LinkedList to mantain the cache queue
        put the used element in the head of the list and remove the tail if reach capacitys
Type: LinkedList
Inpsiration: careful about the head and tail
'''