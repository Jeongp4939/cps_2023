# E : 간선의 수
# N : subtree의 루트 노드
# lst -> 부모-자식 연결관계 순서쌍

for tc in range(1,1+int(input())):
    E,N = map(int,input().split())
    # 노드 번호 1~ E+1번까지 존재
    graph = [[] for _ in range(E+2)]
    lst = list(map(int,input().split()))
    # 인접리스트에 하위 노드 추가
    for i in range(0,E*2,2):
        graph[lst[i]].append(lst[i+1])
    cnt = 1         # 루트 노드 개수 1
    q = graph[N]
    while q:
        node = q.pop(0)
        cnt+=1
        for v in graph[node]:
            q.append(v)

    print(f'#{tc} {cnt}')