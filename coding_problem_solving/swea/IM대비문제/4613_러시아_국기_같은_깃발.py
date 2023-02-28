# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQl9TIK8qoDFAXj

# 위에서 몇 줄(한 줄 이상)은 모두 흰색으로 칠해져 있어야 한다.
# 다음 몇 줄(한 줄 이상)은 모두 파란색으로 칠해져 있어야 한다.
# 나머지 줄(한 줄 이상)은 모두 빨간색으로 칠해져 있어야 한다.

# 가장 위에 한줄을 W로 다 채워야함
# 두번 째 줄 이후 W보다 B가 많으면 B로 채움
# 이후 R이 더 많은 줄 부터는 R로 채움
# -> 맨 아래줄은 다 빨간색

import sys
sys.stdin = open('input.txt','r')

for tc in range(1,int(input())+1):

    n,m = map(int,input().split())
    arr = [list(input()) for _ in range(n)]
    color = ['W','B','R']
    # 1~a, a~b, b~n-1 세 구간을 칠하는 경우의 카운트 중 min값
    Min = 28e8
    cnt=0
    for a in range(1,n-1):
        # B가 한 줄은 나와야 하므로
        for b in range(a+1,n):
            # 첫줄은 칠해야 하므로
            for i in range(0,a):
                cnt+=(m-arr[i].count(color[0]))
            for i in range(a,b):
                cnt+=(m-arr[i].count(color[1]))
            for i in range(b,n):
                cnt+=(m-arr[i].count(color[2]))
            Min = min(Min,cnt)
            cnt = 0

    print(f'#{tc} {Min}')