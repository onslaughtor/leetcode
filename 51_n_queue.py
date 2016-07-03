class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        global ans
        ans=[]
        self.dfs([],n,0,0,0)
        res=[]
        for l in ans:
            res.append([])
            for i in l:
                res[-1].append('.'*i+'Q'+'.'*(n-i-1))
        return res

    def dfs(self,nums,n,left,mid,right):
        if len(nums)==n:
            ans.append([])
            for i in nums:
                ans[-1].append(i)

        for i in range(n):
            k=1<<i
            if (k&(left|mid|right))==0:
                nums.append(i)
                self.dfs(nums,n,(left|k)<<1,mid|k,(right|k)>>1)
                nums.pop()



a=[1,2,3,4,5]
print a[3:0:-1]
print Solution().solveNQueens(4)