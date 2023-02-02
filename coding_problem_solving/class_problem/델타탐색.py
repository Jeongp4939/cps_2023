for tc in range(1,11):

    dx,dy = [0,0,1,-1],[1,-1,0,0]

    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    delta_sum = 0

    for i in range(n):
        for j in range(n):
            for d in range(4):
                if i+dy[d]<0 or j+dx[d]<0 or i+dy[d]>=n or j+dx[d]>=n:
                    continue
                delta_sum+=abs(arr[i+dy[d]][j+dx[d]]-arr[i][j])

    print(f'#{tc} {delta_sum}')