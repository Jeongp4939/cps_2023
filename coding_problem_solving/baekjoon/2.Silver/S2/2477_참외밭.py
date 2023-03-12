# 동1 서2 남3 북4
# 첫 줄 K
# 참외 수 = 넓이 * K
# 반시계 방향으로 둘레를 돌면서 진행

K = int(input())
lst = []

for i in range(6):
    lst.append([*map(int,input().split())])

# 꺾이는 지점을 확인 하기 위해 리스트의 값을 한번 더 반복
# (끝지점에서 꺾이는 경우가 있음)
lst *= 2
curve_point = 0

# 방향이 1-2-1-2 처럼 반복되는 구간 탐색(ㄱ 자의 움푹 들어간 부분)
for i in range(8):
    if lst[i][0]==lst[i+2][0] and lst[i+1][0]==lst[i+3][0]:
        curve_point=i
        break

max_hor = 0
max_ver = 0

# 방향이 1,2일 때 최대값과 3,4일 때의 최대값을 서로 곱해 큰 사각형의 넓이를 구함
for i in lst:
    if i[0] == 1 or i[0] == 2:
        if max_hor<i[1]:
            max_hor=i[1]
    else:
        if max_ver<i[1]:
            max_ver=i[1]
ground = max_ver*max_hor
# 큰 사각형의 넓이에서 작은 사각형의 넓이를 뺀 값을 출력
print((ground - lst[curve_point+1][1]*lst[curve_point+2][1])*K)




