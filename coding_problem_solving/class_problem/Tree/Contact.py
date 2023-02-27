# 마지막에 동시에 연락 받은 사람은 8번, 10번, 17번의 세 명이다.
# 이 중에서 가장 숫자가 큰 사람은 17번이므로 17을 반환하면 된다.

def bfs(st):
    q = [st]
    v[st]=1
    ans = st
    while q:
        c = q.pop(0)
        if v[ans] < v[c] or v[ans]==v[c] and ans<c:
            ans=c

        for i in C[c]:
            if not v[i]:
                q.append(i)
                v[i] = v[c]+1
    return ans


for tc in range(1,11):
    n, st = map(int,input().split())
    lst = list(map(int,input().split()))
    C = [[] for _ in range(101)]
    for i in range(0,n,2):
        C[lst[i]].append(lst[i+1])
    v=[0]*101
    ret = bfs(st)

    print(f'#{tc} {ret}')
