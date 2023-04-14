# 数独
import numpy as np

def is_valid(k: int,row: int,col: int):
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
def is_empty():
    for i in range(9):
        for j in range(9):
            if arr[i][j]==0:
                return True,i,j
    return False,9,9
def sudoku():
    a=is_empty()
    if not a[0]:
        return True
    else:
        i = a[1]
        j = a[2]
    for k in range(1, 10):
        if is_valid(k, i, j):
            arr[i][j] = k
            if sudoku():
                return True
            arr[i][j] = 0
    return False


if __name__ == '__main__':
    arr = np.arange(81).reshape(9, 9)
    print("please input 9 lines and each line has 9 numbers")
    for p in range(9):
        for q, m in enumerate(list(map(int, input().split()))):
            arr[p][q] = m
    sudoku()
    print("The answer of the sudoku is:\n", arr)
