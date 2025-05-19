class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        n,m=len(board),len(board[0])
        new_board=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                live=0 
                cell=board[i][j]
                neigh=[(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,-1),(1,1),(-1,1)]
                for x,y in neigh:
                    ni,nj=i+x,j+y
                    if(0<=ni<n and 0<=nj<m):
                        live+=(board[ni][nj])
                if (cell==1):
                    if(live<2 and live>3):
                        new_board[i][j]=0 
                    elif(live==2 or live==3):
                        new_board[i][j]=1 
                elif(cell==0):
                    if(live==3):
                        new_board[i][j]=1 
        for i in range(n):
            for j in range(m):
                board[i][j]=new_board[i][j]
                