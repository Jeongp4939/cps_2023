from collections import deque

def BFS(st,ed):

    q = deque()
    q.append(st)
    visited[st]=1
    cnt = 0
    while q:
        cnt += 1
        node = q.popleft()
        if ed in lst[node]:
            return visited[i]
        for i in lst[node]:
            if visited[i]==0:
                visited[i]=visited[i]+1
                q.append(i)
            if ed in lst[i]:
                return visited[i]
    return 0

for tc in range(1,int(input())+1):

    v,e = map(int,input().split())

    lst = [[] for _ in range(v+1)]
    visited= [0]*(v+1)
    for i in range(e):
        st,ed = map(int,input().split())
        lst[st].append(ed)
        lst[ed].append(st)
    s,g = map(int,input().split())

    print(f'#{tc} {BFS(s, g)}')
