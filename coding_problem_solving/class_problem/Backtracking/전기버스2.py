def dfs(now=0,cnt=0):
    global Min
    if cnt>Min:
        return
    if now>=n-1 or now+m[now]>=n-1:
        Min = min(cnt,Min)
        return
    for i in range(now,now+m[now]):
        dfs(i+1,cnt+1)

for tc in range(1,1+int(input())):
    n,*m = map(int,input().split())
    Min=28e8
    dfs()
    print(f'#{tc} {Min}')
    # st = 0
    # now = m[0]
    # while st<n:
    #     # n-1 인덱스에 도착 가능하면 종료
    #     if st+m[st]>=n-1:
    #         cnt+=1
    #         break
    #     # now가 1 이상이면 st+=1, now-=1
    #     elif now>0:
    #         st+=1
    #         now-=1
    #     elif now==0:
    #         cnt+=1
    #         now=m[st]
    # print(f'#{tc} {cnt}')
