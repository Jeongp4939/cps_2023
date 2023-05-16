from heapq import heappush as hpush, heappop as hpop
import sys

input = sys.stdin.readline
INF = 1e11

def dijkstra(st, ed):
    q=[]
    hpush(q,(0,st))   # 시작노드 정보 큐에 삽입
    distance = [INF] * (n + 1)
    distance[st] = 0

    while q:
        dist, node = hpop(q)
        # 큐에서 뽑은 거리가 이미 갱신된 거리보다 클 때 무시
        if distance[node] < dist:
            continue
        # 큐에서 뽑은 노드와 연결된 인접 노드 탐색
        for next in graph[node]:
            # 시작 -> node 거리 + node->node 인접노드 거리
            cost = distance[node] + next[1]
            # cost < 시작 -> node 인접노드 거리
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                hpush(q,(cost,next[0]))
    return distance[ed]


n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
mx = -INF

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

for i in range(1,n+1):
    if i==x:
        continue
    res = dijkstra(i,x) + dijkstra(x,i)
    if res<INF:
        mx = max(mx,res)
print(mx)