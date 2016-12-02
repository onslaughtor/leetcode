'''
For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.
'''from collections import deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n==0:
            return []
        pair=[set() for i in xrange(n)]
        for x,y in edges:
            pair[x].add(y)
            pair[y].add(x)
        leaves=[i for i in xrange(n) if len(pair[i])<=1]
        while n>2:
            tmp=[]
            n-=len(leaves)
            for x in leaves:
                y=pair[x].pop()
                pair[y].remove(x)
                if len(pair[y])==1:
                    tmp.append(y)
            leaves=tmp
        return leaves
            
       
        