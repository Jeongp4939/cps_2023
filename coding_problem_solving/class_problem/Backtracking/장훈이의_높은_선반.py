def dfs(n,Sum=0):
    global Min
    # if Sum>Min:
    #     return

    if Min == 0:
        return

    if n==N:
        if Sum >= B:
            Min = min(Min, Sum-B)
        return
    dfs(n+1, Sum+h_lst[n]) # 포함
    dfs(n + 1, Sum) # 포함x


for tc in range(1,1+int(input())):
    Min=int(28e8)
    N,B = map(int,input().split())
    h_lst = list(map(int,input().split()))
    dfs(0,0)

    print(f'#{tc} {Min}')