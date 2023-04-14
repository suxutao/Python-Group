def myfun(k: int, l: list):
    ind = 5
    while ind >= 0:
        if k == 0:
            return 1
        else:
            if l[ind] > 0:
                if k - C[ind] >= 0:
                    k -= C[ind]
                    l[ind] -= 1
                    p = myfun(k, l)
                    if p >= 1:
                        return 1 + p
                    l[ind] += 1
                    k += C[ind]
                    ind -= 1
                else:
                    ind -= 1
            else:
                ind -= 1
    return -1

if __name__ == "__main__":
    K = int(input("input denomination in one number please\n"))
    L = list(map(int, input("input 6 number to show the number of sheet of each type of banknote\n").split()))
    C = [1, 5, 10, 20, 50, 100]
    ans = myfun(K, L) - 1
    if ans == -2:
        print("operation impossible")
    else:
        print(ans)

