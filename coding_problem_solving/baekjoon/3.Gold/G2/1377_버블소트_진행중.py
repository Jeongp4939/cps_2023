# 버블 소트를 진행 하는 중 몇 번째에서 변화가 없는지
# 정렬된 배열이 되는지
# 몇번이 지나가면 정렬이 완료되는지 출력

import sys
input = sys.stdin.readline

n = int(input())
A = [0]
for _ in range(n):
    A.append(int(input()))

# changed = False

# for i in range(1,n+1):
#     changed = False
#     for j in range(1,n-i+1):
#         if A[j] > A[j+1]:
#             changed = True
#             A[j],A[j+1] = A[j+1],A[j]
#     if not changed:
#         print(i)
#         break


