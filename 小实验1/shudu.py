# 数独
def isvalid(arr:list,k:int,row:int,col:int):
    for i in range(9):
        if arr[row][i]==k:
            return False
    for i in range(9):
        if arr[i][col]==k:
            return False
    for i in range(3):
        for j in range(3):
            l=arr[i+(row//3)*3][j+(col//3)*3]
            if k==l:
                return False
    return True
def isempty(arr):
    for i in range(9):
        for j in range(9):
            if arr[i][j]==0:
                return True,i,j
    return False,9,9
def shudu(arr:list):
    a=isempty(arr)
    if not a[0]:
        return True
    else:
        i=a[1]
        j=a[2]
    for k in range(1, 10):
        if isvalid(arr, k, i, j):
            arr[i][j] = k
            if shudu(arr):
                return True
            arr[i][j] = 0
    return False

if __name__ == '__main__':
    arr = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
           [6, 0, 0, 1, 9, 5, 0, 0, 0],
           [0, 9, 8, 0, 0, 0, 0, 6, 0],
           [8, 0, 0, 0, 6, 0, 0, 0, 3],
           [4, 0, 0, 8, 0, 3, 0, 0, 1],
           [7, 0, 0, 0, 2, 0, 0, 0, 6],
           [0, 6, 0, 0, 0, 0, 2, 8, 0],
           [0, 0, 0, 4, 1, 9, 0, 0, 5],
           [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    shudu(arr)
    for i in arr:
        print(i)