for tc in range(1,int(input())+1):

    v, e = map(int,input().split())     # v 노드의 개수, e 간선 정보 개수

    nodes = [[] for _ in range(v+1)]    # 노드 1~V까지(0번은 무시)
    visited = [0]*(v+1)               # 노드 방문 체크 리스트
    stack = []
    # 간선 정보를 받아 리스트 생성
    for i in range(e):
        st,ed = map(int,input().split())
        nodes[st].append(ed)    # 간선 노드 추가
        # nodes[ed].append(st)  # 양방향이면 노드 추가(간선이라 x)

    # 노드 사이 경로의 존재 여부 확인
    st,ed = map(int,input().split())

    stack += nodes[st]       # 시작 노드의 에지 스택에 넣기
    result = 0
    while stack:
        cur_node = stack.pop()      # 현재 노드의 에지(이동할 노드) 스택에서 꺼내오기

        if cur_node == ed:          # 현재 노드가 ed와 같을 때 반복문을 종료하고 끝
            result = 1
            break

        if nodes[cur_node] and not visited[cur_node]: # 비어 있지 않고 방문하지 않았을 때 현재 노드의 원소들 스택 뒤로 빼오기
            visited[cur_node] = 1
            stack+=nodes[cur_node]

    print(f'#{tc} {result}')

