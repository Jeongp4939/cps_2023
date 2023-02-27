for tc in range(1,int(input())+1):
    n = int(input())
    lst = list(map(int,input().split()))
    max_n = min_n = lst[0]
    for i in lst:
        if i > max_n:
            max_n=i
        if i < min_n:
            min_n=i
    print(f'#{tc} {max_n - min_n}')
