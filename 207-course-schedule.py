'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
'''

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        degree={}
        edge=[[] for i in xrange(numCourses)]
        vertex=deque([])
        for p in prerequisites:
            edge[p[0]].append(p[1])
            if p[0] not in degree:
                degree[p[0]]=0
            if p[1] not in degree:
                degree[p[1]]=1
            else:
                degree[p[1]]+=1
        for i in degree:
            if degree[i]==0:
                vertex.append(i)
            
        while len(vertex)>0:
            v=vertex.popleft()
            del degree[v]
            for p in edge[v]:
                degree[p]-=1
                if degree[p]==0:
                    vertex.append(p)
                    
        return len(degree)==0
        
        