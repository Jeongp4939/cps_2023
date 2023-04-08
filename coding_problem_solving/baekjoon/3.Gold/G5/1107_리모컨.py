def dfs(lvl=0,s=''):
    global flag,Min
    if flag:
        return
    if lvl == n_len+1:
        if int(s)==n:
            flag=1
        if Min<abs(n-int(s)):
            Min =  n-int(s)

        return
    for i in btn:
        dfs(lvl+1, s+i)

btn = [str(x) for x in range(10)]
n = int(input())
n_len = len(str(n))
bk_n = input()
if bk_n!='0':
    broken =list(input().split())
    for i in broken:
        btn.remove(i)
flag=0
Min = int(28e8)

if n==100:
    print(0)
else:
    dfs()
    print(min(n_len + Min, abs(100-n)))