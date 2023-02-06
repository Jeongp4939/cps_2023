# 동1 서2 남3 북4
# 첫 줄 K
# 참외 수 = 넓이 * K
# 반시계 방향으로 둘레를 돌면서 진행

K = int(input())
lst = []

for i in range(6):
    lst.append([*map(int,input().split())])

lst *= 2
curve_point = 0

for i in range(8):
    if lst[i][0]==lst[i+2][0] and lst[i+1][0]==lst[i+3][0]:
        curve_point=i
        break

max_hor = 0
max_ver = 0

for i in lst:
    if i[0] == 1 or i[0] == 2:
        if max_hor<i[1]:
            max_hor=i[1]
    else:
        if max_ver<i[1]:
            max_ver=i[1]
ground = max_ver*max_hor

print((ground - lst[curve_point+1][1]*lst[curve_point+2][1])*K)




