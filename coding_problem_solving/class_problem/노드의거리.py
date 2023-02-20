from collections import deque

def BFS(st,ed):
    q = deque([st])
    visited[st]=1
    while q:
        node = q.popleft()
        for n in lst[node]:
            if visited[n]==0:
                if n == ed:
                    return visited[node]
                visited[n]=visited[node]+1
                q.append(n)
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
