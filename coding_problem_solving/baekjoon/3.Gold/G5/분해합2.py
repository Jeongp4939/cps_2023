# https://www.acmicpc.net/problem/12348

def subSum(n):
    tmp = n
    while n>0:
        tmp += n%10
        n//=10
    return tmp
n = int(input())
n_len = len(str(n))
result = 0
for i in range(n-9*n_len,n):
    if subSum(i) == n:
        result = i
        break
print(result)

