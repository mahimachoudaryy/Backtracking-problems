"""
Rat in a Maze Problem (Backtracking)
Finding all possible paths from (0,0) to (n-1,n-1) in a maze of size nxn.
"""
class Solution:
    def ratInMaze(self, maze):
        # code here
        def backtrack(row,col,directions,maze,res,ans,n):
            if (row==n-1 and col==n-1):
                ans.append(res)
                return
            for r,c,d in directions:
                nr=row+r
                nc=col+c
                if(nr>=0 and nr<n and nc>=0 and nc<n and maze[nr][nc]==1):
                    maze[nr][nc]="."
                    backtrack(nr,nc,directions,maze,res+d,ans,n)
                    maze[nr][nc]=1
        directions=[[1,0,'D'],[0,-1,'L'],[0,1,'R'],[-1,0,'U']]
        n=len(maze)
        row,col=0,0
        maze[row][col]="."
        ans=[]
        res=""
        backtrack(row,col,directions,maze,res,ans,n)
        return ans