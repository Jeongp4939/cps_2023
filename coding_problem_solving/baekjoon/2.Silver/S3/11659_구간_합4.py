import sys
input = sys.stdin.readline

n,m = map(int,input().split())
n_lst = list(map(int,input().split()))
sum_lst = [0]
tmp = 0

for i in n_lst:
    tmp += i
    sum_lst.append(tmp)

for _ in range(m):
    i,j = map(int,input().split())
    print(sum_lst[j]-sum_lst[i-1])