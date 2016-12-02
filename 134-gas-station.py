'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
'''
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n=len(gas)
        for i in xrange(n):
            gas[i]-=cost[i]
        start=n
        end=0
        m=0
        while end!=start:
            if m+gas[end]>=0:
                m+=gas[end]
                end+=1
            else:
                start-=1
                m+=gas[start]
        if m>=0:
            return start%n
        else:
            return -1
               