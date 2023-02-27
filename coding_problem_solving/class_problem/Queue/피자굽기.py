from collections import deque

for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    c = list(map(int,input().split()))
    piz = deque(map(list,enumerate(c,start=1)))
    q = deque()

    for _ in range(n):
        q.append(piz.popleft())

    while len(q)!=1:

        q[0][1]//=2

        if q[0][1]==0:
            q.popleft()
            if piz:
                q.append(piz.popleft())
        else:
            q.append(q.popleft())



    print(f'#{tc} {q[0][0]}')