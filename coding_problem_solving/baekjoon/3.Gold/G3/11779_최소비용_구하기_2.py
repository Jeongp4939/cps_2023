import heapq
import sys
input = sys.stdin.readline
INF = 10e8

def dijkstra(n,st):
    distances = [[INF,[]] for _ in range(n + 1)]
    distances[st][0] = 0
    distances[st][1].append(st)

    q = []

    heapq.heappush(q, [distances[st][0], st])

    while q:
        dist, node = heapq.heappop(q)

        if distances[node][0] < dist:
            continue

        for new_node, new_dist in graph[node]:
            distance = dist + new_dist
            if distance < distances[new_node][0]:
                distances[new_node][0] = distance
                distances[new_node][1] = distances[node][1]+[new_node]
                heapq.heappush(q, [distance, new_node])
    return distances

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b,dist = map(int,input().split())
    graph[a].append([b,dist])

st,ed = map(int,input().split())

distance = dijkstra(n,st)
print(distance[ed][0])
print(len(distance[ed][1]))
print(*distance[ed][1])


