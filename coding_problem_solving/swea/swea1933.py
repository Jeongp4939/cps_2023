# 약수 출력

N = int(input())
divisor = []

for n in range(1, N+1):
    if N % n == 0:
        divisor.append(n)
print(*divisor)