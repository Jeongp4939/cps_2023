for tc in range(1,1+int(input())):
    n,m = map(int,input().split())
    wlst = list(map(int,input().split()))
    tlst = list(map(int, input().split()))
    wlst.sort(reverse=True)
    tlst.sort(reverse=True)

    wi=ti=0
    cnt = 0
    while wi < n and ti < m:
        if wlst[wi] <= tlst[ti]:
            cnt+=wlst[wi]
            wi+=1
            ti+=1
        else:
            wi+=1

    print(f'#{tc} {cnt}')