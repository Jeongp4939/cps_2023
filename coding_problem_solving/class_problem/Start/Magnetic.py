# 1은 N극 성질을 가지는 자성체를 2는 S극 성질을 가지는 자성체를 의미하며
# 테이블의 윗부분에 N극이 아래부분에 S극이 위치한다고 가정한다
# 1-> 아래로 이동
# 2-> 위로 이동
import sys
sys.stdin = open('input.txt','r')
#
# dy = [1,-1]
#
# def isdrop(y,x):
#     flag=0
#     # N극 아래로 이동
#     if arr[y][x]==1:
#         d = y+dy[0]
#         # 아래방향에 S극에 해당하는 자석이 있는지 판별
#         # 이동 방향에 다른 색의 자석을 만나기 전에 같은 색의 자석을 만나면 flag 1
#         while 0<=d<n:
#             if arr[d][x]==1:
#                 flag=1
#             elif arr[d][x]==2:
#                 if flag:
#                     return 0
#                 return 1
#
#             d+=dy[0]
#         return 0
#     # S극 위로 이동
#     elif arr[y][x]==2:
#         d = y+dy[1]
#         # 윗방향에 N극에 해당하는 자석이 있는지 판별
#         while 0<=d<n:
#             if arr[d][x]==2:
#                 flag=1
#             elif arr[d][x]==1:
#                 if flag:
#                     return 0
#                 return 1
#             d+=dy[1]
#         return 0
#     return 0
#
# T=10
# for tc in range(1,1+T):
#
#     n=int(input())
#     arr=[list(map(int,input().split())) for _ in range(n)]
#     rlt = 0
#     for i in range(n):
#         for j in range(n):
#             rlt+=isdrop(i,j)
#
#     print(f'#{tc} {rlt}')
#

def isdrop(y,x):
    flag=0
    # N극 아래로 이동
    if arr[y][x]==1:
        d = y+1
        # 아래방향에 S극에 해당하는 자석이 있는지 판별
        # 이동 방향에 다른 색의 자석을 만나기 전에 같은 색의 자석을 만나면 flag 1
        while 0<=d<n:
            if arr[d][x]==1:
                flag=1
            elif arr[d][x]==2:
                if flag:
                    return 0
                return 1
            d+=1
        return 0
    return 0

T=10
for tc in range(1,1+T):

    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    rlt = 0
    for i in range(n):
        for j in range(n):
            rlt+=isdrop(i,j)

    print(f'#{tc} {rlt}')
