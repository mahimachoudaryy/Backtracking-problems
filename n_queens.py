"""
N-Queens Problem (Backtracking)
Place N queens on an nxn chessboard such that no two queens attack each other.
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def canWePlace(row,col,mat):
            #Checking top-left
            r,c= row,col
            while(r>=0 and c>=0):
                if(mat[r][c]=='Q'):
                    return False
                r-=1
                c-=1
            #Checking top
            r,c=row,col
            while(r>=0):
                if(mat[r][c]=='Q'):
                    return False
                r-=1
            #Checking top-right
            r,c=row,col
            while(r>=0 and c<n):
                if(mat[r][c]=='Q'):
                    return False
                r-=1
                c+=1
            return True
        def backtrack(row,mat,ans,n):
            if (row==n):
                  temp=[]
                  for r in mat:
                      temp.append(''.join(r))
                  ans.append(temp)
                  return
            for col in range(0,n):
                  if(canWePlace(row,col,mat)):
                      mat[row][col]="Q"
                      backtrack(row+1,mat,ans,n)
                      mat[row][col]="."
        mat=[]
        for i in range(0,n):
            lst=['.']*n
            mat.append(lst)
        row=0
        ans=[]
        backtrack(row,mat,ans,n)
        return ans 