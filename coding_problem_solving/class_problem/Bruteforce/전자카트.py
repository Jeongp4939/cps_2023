def calc_sum(level=0, idx=0, Sum=0):
    global Min
    if level==n:
        Min = min(Min,Sum)
        return

    if level==0:
        for i in range(1,n):
            if not used[i]:
                used[i]=1
                calc_sum(level+1,i,Sum+lst[0][i])
                used[i]=0
    elif level==n-1:
        calc_sum(level+1,idx,Sum+lst[idx][0])
    else:
        for i in range(1,n):
            if not used[i]:
                used[i]=1
                calc_sum(level+1,i,Sum+lst[idx][i])
                used[i] = 0


for tc in range(1,1+int(input())):
    n = int(input())
    lst = []
    used = [0] * n
    Min = int(28e8)
    for _ in range(n):
        lst.append(list(map(int,input().split())))

    # 방문한 지점은 다시 가지 않음, 시작지점 1, 마지막 지점 1
    calc_sum(0)


    print(f'#{tc} {Min}')