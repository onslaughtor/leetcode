class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n=len(board)
        if n==0:
            return 
        m=len(board[0])
        from collections import deque
        q=deque([])
        for i in xrange(m):
            self.check(board,0,i,q)
            self.check(board,n-1,i,q)
        for i in xrange(n):
            self.check(board,i,0,q)
            self.check(board,i,m-1,q)

        while len(q)>0:
            x=q.popleft()
            self.check(board,x[0]-1,x[1],q)
            self.check(board,x[0]+1,x[1],q)
            self.check(board,x[0],x[1]-1,q)
            self.check(board,x[0],x[1]+1,q)
            
        for i in xrange(n):
            for j in xrange(m):
                if board[i][j]=='Y':
                    board[i][j]='O'
                else:
                    board[i][j]='X'
                
    def check(self,board,i,j,q):
        if i>=0 and i<len(board) and j>=0 and j<len(board[i]) and board[i][j]=='O':
            board[i][j]='Y'
            q.append((i,j))



