# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 신청서 N이 주어지고,
# 다음 줄부터 N개의 줄에 걸쳐 화물차의 작업 시작 시간 s와 종료 시간 e가 주어진다.
# 1<=N<=100, 0<=s<24, 0 ＜ e ＜= 24

# 시작 시간을 노드의 헤드로 하고, 종료 시간을 노드의 간선으로 생각하고 DFS를 시행하면 해결 가능할 것 같음
import sys
sys.stdin = open('input.txt','r')

for tc in range(1,1+int(input())):
    n=int(input())
    A = [list(map(int,input().split())) for _ in range(n)]
    # A를 시작 시간으로 먼저 sort 한 후
    # 끝 시간으로 다시 한번 sort
    A = sorted(A, key=lambda x:(x[1],x[0]))
    # 1번 인덱스부터 검사하므로 cnt+1, i=1
    cnt=1
    i=1
    # A의 첫 인덱스의 끝 시간을 저장
    now = A[0][1]

    while i<n:
        # idx번째 원소를 가져와서 시작 시간이 now보다 크면
        # now를 idx번째 원소의 끝으로 바꿔주고 cnt+=1
        s,e=A[i]

        if s >= now:
            now=e
            cnt += 1
        # 다음번 원소를 검사하기위해 i+1
        i+=1

    print(f'#{tc} {cnt}')