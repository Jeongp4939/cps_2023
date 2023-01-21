# 파스칼의 삼각형
memo={0:1,1:1}
def factorial_memo(n):
    if n in memo:
        return memo[n]
    memo[n] = factorial_memo(n-1)*n
    return memo[n]
def combination(n,r):
    return factorial_memo(n)//(factorial_memo(n-r)*factorial_memo(r))

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    pascal_triangle = []
    for n in range(N):
        lst=[]
        for i in range(n+1):
            lst.append(combination(n, i))
        pascal_triangle.append(lst)
    print(f'#{tc}')
    for line in pascal_triangle:
        print(*line)
