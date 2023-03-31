
def dfs(n,sm):
    global ans
    if ans <= sm:
        return
    if n>12:
        ans = min(ans,sm)
        return

    dfs(n+1, sm+day*lst[n]) # 일간
    dfs(n+1, sm+mon)        # 월
    dfs(n+3, sm+mon3)      # 분기
    dfs(n+12, sm+year)      # 연간


T = int(input())
for tc in range(1,T+1):
    day, mon, mon3, year = map(int,input().split())
    lst = [0]+list(map(int,input().split()))

    # 백트래킹
    # ans = 365*3000
    # dfs(1,0)

    # 규칙성 찾기
    s = [0]*13
    for i in range(1,13):
        # 가능한 방법중 i 달의 최소 비용 갱신
        s[i] = s[i-1]+day*lst[i]    # 일간권
        s[i] = min(s[i], s[i-1]+mon)
        if i >= 3:
            s[i] = min(s[i], s[i - 3] + mon3)
        if i >= 12:
            s[i] = min(s[i], s[i-12] + year)

    ans = s[12]
    print(f'#{tc} {ans}')
