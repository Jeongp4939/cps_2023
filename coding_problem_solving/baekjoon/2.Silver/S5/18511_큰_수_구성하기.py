def dfs(depth=0, num=0):
    global MAX
    if num>n:
        return
    if num <= n:
        MAX = max(MAX, num)
    if depth==n_len:
        return
    for i in range(k):
        dfs(depth+1,num*10+li[i])

n,k = map(int,input().split())
n_len = len(str(n))
li = list(map(int,input().split()))
li.sort(reverse=True)

MAX = -28e9

dfs()

print(MAX)
