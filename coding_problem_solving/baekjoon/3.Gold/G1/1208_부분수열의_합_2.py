import sys
from collections import defaultdict
input = sys.stdin.readline

N,S = map(int, input().split())
N_list = list(map(int,input().split()))
A, B = defaultdict(int), defaultdict(int)
for i in range(1<<(N//2)):
    cnt = 0
    for j in range(N//2):
        if i & (1<<j):
            cnt += N_list[:N//2][j]
    A[cnt] += 1
for i in range(1<<(N-N//2)):
    cnt = 0
    for j in range(N-N//2):
        if i & (1<<j):
            cnt += N_list[N//2:][j]
    B[cnt] += 1
ans = 0
for b in B:
    ans += A[S-b]*B[b]
if S == 0:
    print(ans-1)
else:
    print(ans)