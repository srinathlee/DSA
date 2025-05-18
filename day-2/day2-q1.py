# zero fill matrix
# if any element in the matrix is zero the the corresponding row and col element should be 0

matrix=[[1,0,2],[2,4,5],[5,0,7]]

is_first_row_0=False
is_first_col_0=False 
        
for i in range(len(matrix[0])):
    if matrix[0][i]==0:
        is_first_row_0=True 
for j in range(len(matrix)):
    if matrix[j][0]==0:
        is_first_col_0=True
        
for i in range(1,len(matrix)):
    for j in range(1,len(matrix[0])):
        if(matrix[i][j]==0):
            matrix[0][j]=0 
            matrix[i][0]=0 
for i in range(1,len(matrix)):
    for j in range(1,len(matrix[0])):
        if(matrix[0][j]==0):
            matrix[i][j]=0 
        if(matrix[i][0]==0):
            matrix[i][j]=0 
if(is_first_row_0):
    for i in range(len(matrix[0])):
        matrix[0][i]=0 
if(is_first_col_0):
    for j in range(len(matrix)):
        matrix[j][0]=0
print(matrix)
    