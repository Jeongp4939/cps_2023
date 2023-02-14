def calc(n, sum_n=0):
    global min_n
    if min_n<sum_n:
        return
    if n<0:
        if min_n > sum_n:
            min_n=sum_n
        return

    for i in range(len(arr[n])):
        if visited[i]:
            continue
        else:
            visited[i]=1
            sum_n += arr[n][i]
            calc(n-1,sum_n)
            sum_n -= arr[n][i]
            visited[i]=0

for tc in range(1,int(input())+1):

    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [0]*n
    min_n = 10e28
    calc(n-1)
    print(f'#{tc} {min_n}')