from heapq import heappush as hpush, heappop as hpop
import sys

input = sys.stdin.readline
INF = 1e11

def dijkstra(st,ed):
    q = []
    hpush(q, (0, st))  # 시작노드 정보 큐에 삽입
    distance = [INF] * (N + 1)
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

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

st,ed = map(int,input().split())

res = dijkstra(st,ed)

if res<INF:
    print(res)
else:
    print(-1)