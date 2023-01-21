# 흑돌과 백돌
# 흑돌 i/i+1 백돌 1/i+1 -> 임의의 숫자 5개의 곱의 합을 구해야 함
from itertools import combinations

memo = {0: 1, 1: 1}

def factorial_memo(n):
    if n in memo:
        return memo[n]
    memo[n] = factorial_memo(n - 1) * n
    return memo[n]


# T = int(input())
N, K, M = map(int, input().split())

lst = list(combinations(range(1,N+1), K))
lst_multiple = []

for ls in lst:
    mul = 1
    for i in ls:
        mul *= i
    lst_multiple.append(mul)
print(sum(lst_multiple))
