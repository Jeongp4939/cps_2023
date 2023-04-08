def find(x):
    if x != graph[x]:
        return find(graph[x])
    return graph[x]


def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        graph[a] = b
    else:
        graph[b] = a


for testcase in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(e)]
    # 가중치를 기준으로 정렬
    sorted_lst = sorted(lst,key=lambda x:x[2])
    graph = [0] * (v + 1)
    result = 0
    cnt = 0
    for i in range(v + 1):
        graph[i] = i
    for i in sorted_lst:
        start, end, cost = i
        # 사이클 생성을 방지
        if find(start) != find(end):
            cnt += 1
            result += cost
            union(start, end)
        if cnt == v:
            print(f'#{testcase} {result}')
            break