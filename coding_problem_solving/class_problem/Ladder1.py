# import sys
# sys.stdin = open('input.txt','r')
#
# import copy
#
# dy,dx = [1,0,0],[0,-1,1]
#
# def ladder(ar,x,y=0):
#     new_ar = copy.deepcopy(ar)
#     start = []
#     start.append([y,x])
#
#     while start:
#         y, x = start.pop()
#
#         for i in range(1,3):
#             ny = y+dy[i]
#             nx = x+dx[i]
#
#             if 0<=ny<100 and 0<=nx<100 and new_ar[ny][nx]:
#                 if new_ar[ny][nx] == 2:
#                     return 1
#                 new_ar[ny][nx]=0
#                 start.append([ny,nx])
#                 break
#
#         else:
#             ny = y+dy[0]
#             nx = x+dx[0]
#
#             if 0<=ny<100 and 0<=nx<100 and new_ar[ny][nx]:
#                 if new_ar[ny][nx] == 2:
#                     return 1
#                 new_ar[ny][nx]=0
#                 start.append([ny,nx])
#
#     return 0
#
# for tc in range(1,11):
#     input()
#     arr = [list(map(int,input().split())) for _ in range(100)]
#     result = 0
#     for i in range(100):
#         if arr[0][i]==1 and ladder(arr,i):
#             result = i
#     print(f'#{tc} {result}')
#

#
# import sys
# sys.stdin = open('input.txt','r')
#
# import copy
#
# dy,dx = [-1,0,0],[0,-1,1]
#
# def ladder(ar,x,y=99):
#     new_ar = copy.deepcopy(ar)
#     start = []
#     start.append([y,x])
#
#     while start:
#         y, x = start.pop()
#
#         for i in range(1,3):
#             ny = y+dy[i]
#             nx = x+dx[i]
#
#             if 0<=ny<100 and 0<=nx<100 and new_ar[ny][nx]:
#                 if ny==0:
#                     return nx
#                 new_ar[ny][nx]=0
#                 start.append([ny,nx])
#                 break
#
#         else:
#             ny = y+dy[0]
#             nx = x+dx[0]
#
#             if 0<=ny<100 and 0<=nx<100 and new_ar[ny][nx]:
#                 if ny==0:
#                     return nx
#                 new_ar[ny][nx]=0
#                 start.append([ny,nx])
#
#     return 0
#
# for tc in range(1,11):
#     input()
#     arr = [list(map(int,input().split())) for _ in range(100)]
#     result = 0
#     for i in range(100):
#         if arr[99][i]==2:
#             result = ladder(arr,i)
#     print(f'#{tc} {result}')