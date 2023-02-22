def find(node):
    if not graph[node]:
        if len(graph)-1 < node*2:   # 그래프의 길이= node의 수 +1
            return graph[node]
        elif len(graph)-1 < node*2+1:
            return graph[node*2]
        else:
            return graph[node*2]+graph[node*2+1]
    else:
        return graph[node]


for tc in range(1,1+int(input())):


    n,m,l = map(int,input().split())
    graph = [0] * (n+1)
    for i in range(m):
        node, num = map(int,input().split())
        graph[node]=num
    for i in range(n,-1,-1):
        graph[i]=find(i)

    print(f'#{tc} {graph[l]}')