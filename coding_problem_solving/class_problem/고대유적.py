def count(ar):
    mx= 0
    for lst in ar:
        cnt = 0
        for i in lst:
            if i==1:
                cnt+=1
                if mx<cnt:
                    mx = cnt
            else:
                cnt=0
    return mx

for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    arr_t = list(map(list,zip(*arr)))

    ans = count(arr)
    t = count(arr_t)
    if ans<t:
        ans=t

    print(f'#{tc} {ans}')

