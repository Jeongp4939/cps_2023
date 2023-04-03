
def dfs(depth, st, w=0):
    global Min
    if depth == v:
        Min = min(Min,w)
        return
    for i in graph[st]:
        if not visited[i[0]]:
            visited[i[0]] = 1
            dfs(depth+1, i[0], w+i[1])
            visited[i[0]] = 0

for tc in range(1, 1+int(input())):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        n1,n2,w = map(int,input().split())
        graph[n1].append((n2,w))
        graph[n2].append((n1,w))

    Min =int(21e8)
    for i in range(v+1):
        visited = [0]*(v+1)
        visited[i]=1
        dfs(0,i)
    print(f'#{tc} {Min}')
