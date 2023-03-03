def calc_sum(lvl=0,Sum=0):
    global Min
    if Sum>Min:
        return
    if lvl==n:
        Min = min(Sum,Min)
        return
    for i in range(n):
        if not visited[i]:
            visited[i]=1
            calc_sum(lvl+1,Sum+arr[lvl][i])
            visited[i]=0


for tc in range(1,1+int(input())):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited=[0]*n
    Min = int(28e8)

    calc_sum()

    print(f'#{tc} {Min}')