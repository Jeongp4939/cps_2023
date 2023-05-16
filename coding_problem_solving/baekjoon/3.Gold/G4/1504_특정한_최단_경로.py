from heapq import heappush as hpush, heappop as hpop
import sys

input = sys.stdin.readline
INF = 1e11

def dijkstra(st,ed):
    q = []
    hpush(q, (0, st))  # 시작노드 정보 큐에 삽입
    distance = [INF] * (E + 1)
    distance[st] = 0

    while q:
        dist, node = hpop(q)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                hpush(q, (cost, next[0]))
    return distance[ed]

E,V = map(int,input().split())
graph = [[] for _ in range(E+1)]

for _ in range(V):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

path1,path2 = map(int,input().split())

res1 = dijkstra(1,path1) + dijkstra(path1,path2) + dijkstra(path2,E)
res2 = dijkstra(1,path2) + dijkstra(path2,path1) + dijkstra(path1,E)
res = min(res1,res2)
if res<INF:
    print(res)
else:
    print(-1)