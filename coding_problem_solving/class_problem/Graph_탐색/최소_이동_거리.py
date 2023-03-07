# 간선은 일방통행이다
# N번 노드에 도착할 때까지 진행
# 최소비용 구하기

def dfs(now=0,Sum=0):
    global Min
    if Sum>Min:
        return
    if now==n:
        Min = min(Min,Sum)
        return
    for i in node[now]:
        dfs(i[0],Sum+i[1])

for tc in range(1,1+int(input())):
    n,e = map(int,input().split())
    # 0 ~ n 번까지의 노드 존재
    node = [[] for _ in range(n+1)]
    Min = int(28e8)
    for i in range(e):
        s,e,w = map(int,input().split())
        node[s].append([e,w])
    dfs()
    print(f'#{tc} {Min}')
