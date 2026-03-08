"""
Sudoku Solver(Backtracking)
Solving a 9x9 Sudoku puzzle by filling the empty cells.
"""
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n=9
        def CanWePlace(row,col,num,board):
            for i in range(0,n):
                if (board[row][i]==num or board[i][col]==num):
                    return False
            start_row,start_col=3*(row//3),3*(col//3)
            for i in range(start_row,start_row+3):
                for j in range(start_col,start_col+3):
                    if (board[i][j]==num):
                        return False
            return True
        def SolveSudoku(board):
            for row in range(0,n):
                for col in range(0,n):
                    if (board[row][col]=='.'):
                        for num in '123456789':
                            if (CanWePlace(row,col,num,board)):
                                board[row][col]=num
                                if(SolveSudoku(board)):
                                    return True
                                board[row][col]='.'
                        return False
            return True
        return SolveSudoku(board)