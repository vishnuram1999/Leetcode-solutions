matrix = [[1,2,3],[4,5,6],[7,8,9]]
def nearby(row, col):
    l = []
    if row-1>=0 and col-1>=0 and row-1<len(matrix) and col-1<len(matrix):
        l.append([row-1,col-1])
    if row-1>=0 and col>=0 and row-1<len(matrix) and col<len(matrix):
        l.append([row-1,col])
    if row-1>=0 and col+1>=0 and row-1<len(matrix) and col+1<len(matrix):
        l.append([row-1,col+1])
    if row>=0 and col-1>=0 and row<len(matrix) and col-1<len(matrix):
        l.append([row,col-1])
    if row>=0 and col+1>=0 and row<len(matrix) and col+1<len(matrix):
        l.append([row,col+1])
    if row+1>=0 and col-1>=0 and row+1<len(matrix) and col-1<len(matrix):
        l.append([row+1,col-1])
    if row+1>=0 and col>=0 and row+1<len(matrix) and col<len(matrix):
        l.append([row+1,col])
    if row+1>=0 and col+1>=0 and row+1<len(matrix) and col+1<len(matrix):
        l.append([row+1,col+1])
    
    return l

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        list1=nearby(i,j)
        print([i,j], list1)