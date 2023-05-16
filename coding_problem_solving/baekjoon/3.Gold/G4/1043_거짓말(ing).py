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

N,M = list(map(int,input().split()))
truth = list(map(int,input().split()))[1:]

KNOW_TRUTH = 0
# 부모리스트 -> 0은 진실을 아는 사람
parent = list(range(N+1))
for person in truth:
    parent[person] = KNOW_TRUTH

ans = 0
parties = []

for _ in range(M):
    party = list(map(int,input().split()))[1:]
    for i in range(len(party)-1):
        union(party[i],party[i+1])
    parties.append(party)

for party in parties:
    know = False
    for i in range(len(party)):
        if find(party[i]) == KNOW_TRUTH:
            know = True
            break
    if not know:
        ans += 1

print(ans)