# https://www.acmicpc.net/problem/2798

def recur(lvl=0,idx=0,Sum=0):
    global n,m, Max
    if lvl==3:
        if Sum<=m:
            Max=max(Sum,Max)
        return
    for i in range(n):
        if i>=idx:
            recur(lvl+1,i+1,Sum+lst[i])

Max=0
n,m = map(int,input().split())
lst = list(map(int,input().split()))
recur()
print(Max)
