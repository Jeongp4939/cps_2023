# https://www.acmicpc.net/problem/1966
# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
# 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
# 각 값에 대해서 뒤쪽으로 우선순위가 높은 게 있는지 확인
# ->브루트포스?

from collections import deque

tc = int(input())
for t in range(tc):
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    q = deque()
    for idx,w in enumerate(A):
        q.append([idx,w])
    i = cnt = 0
    while q:
        if not q[i][1] == max(q,key=lambda x:x[1])[1]:
            q.append(q.popleft())
        elif q[i][1] == max(q,key=lambda x:x[1])[1]:
            pr = q.popleft()[0]
            cnt+=1
            if pr == m:
                break
    print(cnt)















