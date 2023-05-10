# 버블 소트를 진행 하는 중 몇 번째에서 변화가 없는지
# 정렬된 배열이 되는지
# 몇번이 지나가면 정렬이 완료되는지 출력

import sys
input = sys.stdin.readline

n = int(input())
A = []
for i in range(n):
    A.append((int(input()),i))

Max = 0
sorted_A = sorted(A)

for i in range(n):
    Max=max(Max,sorted_A[i][1]-i)
print(Max + 1)