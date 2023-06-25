import heapq

n,k = map(int,input().split())
gems = []
bags = []

for _ in range(n):
    m,v = map(int,input().split())
    gems.append((m,v))

for _ in range(k):
    c = int(input())
    bags.append(c)

gems.sort()
bags.sort()

result = 0
tmp = []

for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(tmp, -gems[0][1])
        heapq.heappop(gems)
    if tmp:
        result -= heapq.heappop(tmp)
print(result)