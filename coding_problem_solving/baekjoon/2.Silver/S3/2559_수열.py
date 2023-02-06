# 2<=N<=100000, 1<=K<=N
# 배열의 숫자는 -100 이상 100 이하
N, K = map(int,input().split())
lst = list(map(int, input().split()))
result = [0]*(N-K+1)

for i in range(N-K+1):
    if i == 0:
        result[i] = sum(lst[i:i+K])
    else:
        result[i] = result[i-1]-lst[i-1]+lst[i+K-1]
print(max(result))

# Sliding Window Algorithm 공부
