'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''
from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        queue=deque([])
        n=len(board)
        if n==0:
            return 
        m=len(board[0])
        for i in xrange(m):
            self.check(board,0,i,queue)
            self.check(board,n-1,i,queue)
        for i in xrange(1,n-1):
            self.check(board,i,0,queue)
            self.check(board,i,m-1,queue)
            
        while len(queue)>0:
            x,y=queue.popleft()
            self.check(board,x-1,y,queue)
            self.check(board,x+1,y,queue)
            self.check(board,x,y-1,queue) 
            self.check(board,x,y+1,queue)  
        for x in xrange(n):
            for y in xrange(m):
                if board[x][y]=='Y':
                    board[x][y]='O'
                else:
                    board[x][y]='X'
                    
        
    def check(self,board,x,y,queue):
        if x>=0 and x<len(board) and y>=0 and y<len(board[x]) and board[x][y]=='O':
            board[x][y]='Y'
            queue.append((x,y))
        