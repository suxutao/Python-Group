# 最少要用多少张纸币--贪心算法
choice=[]
def myfun(K:int, L:list):
    K_pre=K
    L_pre=[[100, L[0]], [50, L[1]], [20, L[2]], [10, L[3]], [5, L[4]], [1, L[5]]]
    if K==0:
        return 0
    for x in range(6):
        # 初始化
        K_now=K_pre
        L_now = [L_pre[0].copy(), L_pre[1].copy(), L_pre[2].copy(), L_pre[3].copy(), L_pre[4].copy(), L_pre[5].copy(), 0]
        result=0

        while K_now >= L_now[x][0] and L_now[x][1] > 0:
            K_now -= L_now[x][0]
            result += 1
            L_now[x][1] -= 1
            if K_now == 0:
                choice.append(result)

        for z in range(x+1,6):
            L_now2=[L_now[0].copy(),L_now[1].copy(),L_now[2].copy(),L_now[3].copy(),L_now[4].copy(),L_now[5].copy(),0]
            K_now2=K_now
            result2=result
            for y in range(z,6):
                while K_now2>=L_now2[y][0] and L_now2[y][1]>0:
                    K_now2-=L_now2[y][0]
                    result2+=1
                    L_now2[y][1]-=1
                    if K_now2==0:
                        choice.append(result2)
    if len(choice)>0:
        return min(choice)
    else:
        return 'impossible'

if __name__ == '__main__':
    K=int(input())
    L=list(map(int,input().split()))
    L.reverse()
    print(myfun(K,L))