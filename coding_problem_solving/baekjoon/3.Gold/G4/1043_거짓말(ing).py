
def find(x):
    if x!=parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b



N,M = map(int,input().split())
truth = list(map(int,input().split()))[1:]
parties = []
parent = list(range(1+N))

for i in range(M):
    parties.append(list(map(int,input().split())))
print(parties)

