class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        col=[set([]) for i in range(9)]
        row=[set([]) for i in range(9)]
        grid=[set([]) for i in range(9)]
        task=[]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    col[i].add(int(board[i][j]))
                    row[j].add(int(board[i][j]))
                    grid[(i/3)*3+(j/3)].add(int(board[i][j]))
                else:
                    task.append((i,j))
        print self.search(col,row,grid,board,task)

    def search(self,col,row,grid,board,task):
        if len(task)==0:
            return 1
        i,j=task.pop()
        for k in range(1,10):
            if k not in col[i] and k not in row[j] and k not in grid[(i/3)*3+(j/3)]:
                board[i][j]=str(k)
                col[i].add(k)
                row[j].add(k)
                grid[(i/3)*3+(j/3)].add(k)
                if self.search(col,row,grid,board,task)==1:
                    return 1
                col[i].remove(k)
                row[j].remove(k)
                grid[(i/3)*3+(j/3)].remove(k)
        task.append((i,j))
        return 0 
        
        

tmp=["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board=[]
for i in tmp:
    board.append(list(i))
Solution().solveSudoku(board)
print board
#["519748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]

 