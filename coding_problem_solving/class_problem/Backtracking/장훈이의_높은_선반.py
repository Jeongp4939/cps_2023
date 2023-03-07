def dfs(lvl,b,idx=0,Sum=0):
    global Min
    if Sum>Min:
        return
    if lvl==n:
        if Sum >= b:
            Min = min(Min, Sum)
        return
    if Sum>=b:
        Min = min(Min,Sum)
    for i in range(n):
        if i>=idx:
            dfs(lvl+1,b,i+1,Sum+h_lst[i])


for tc in range(1,1+int(input())):
    Min=int(28e8)
    n,b = map(int,input().split())
    h_lst = list(map(int,input().split()))
    dfs(0,b)

    print(f'#{tc} {Min-b}')