for tc in range(1,int(input())+1):

    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    switch = [0]*n
    min_n = 11

    print(f'#{tc}')