# brute force technique of BigO(n2)
def setzero(matrix:list)->list:
    getrw=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==0:
                getrw.append([i,j])
    # set zero to column
    for i in getrw:
        row=i[0]
        col=i[1]
        for i in matrix:
            i[col]=0
        for i in range(len(matrix[0])):
            matrix[row][i]=0
    print(matrix)
    return

setzero([[7,1,2],[3,0,0],[7,9,7]])