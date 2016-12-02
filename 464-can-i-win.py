'''
In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.
What if we change the game so that players cannot re-use integers?
For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.
Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.
You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.
'''
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal<=0:
            return True
        if maxChoosableInteger*(maxChoosableInteger+1)/2<desiredTotal:
            return False
        self.dp={}
        return self.minmax((1<<maxChoosableInteger)-1,desiredTotal)
        
    def minmax(self,nums,target):
        if target<=0:
            return False
        if nums in self.dp:
            return self.dp[nums]
        else:
            self.dp[nums]=False
        i=1
        mask=1
        while mask<=nums:
            if nums&mask>0 and not self.minmax(nums^mask,target-i):
                self.dp[nums]=True
                break
            mask<<=1
            i+=1
        return self.dp[nums]