'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(ratings)
        ans=[1]*n
        for i in xrange(1,n):
            if ratings[i]>ratings[i-1]:
                ans[i]=ans[i-1]+1

        for i in xrange(n-2,-1,-1):
            if ratings[i]>ratings[i+1] and ans[i+1]+1>ans[i]:
                ans[i]=ans[i+1]+1
        return sum(ans)


'''
Solution:
    find the peak and bottom of the rating curve to make some slope, 
    assign the bottom with one candy then add one by one from bottom to peak,
    assign the length of longer slope to the peak
type: Greedy
Inspiration: draw the picture and find the pattern
'''





     