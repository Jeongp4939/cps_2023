def dfs(n,sm):
    global ans
    # 가지치기 : 더이상 정답 갱신 가능성 없을 때 하는 것
    #
    # if K < sm:
    #     return

    if n == N :
        if sm==K:
            ans+=1
        return

    dfs(n+1, sm+lst[n]) # 포함
    dfs(n+1, sm)        # 포함 X


T = int(input())
for tc in range(1, T+1):
    N, K  = map(int, input().split())
    lst = list(map(int,input().split()))

    ans = 0
    dfs(0,0)

    print(f'#{tc} {ans}')