def dfs(n,l,idx=0,t=0,k=0):
    global Max_t,Max_k
    if k>l:
        return
    if Max_t < t and k<=l:
        Max_k = k
        Max_t = t
    for i in range(n):
        if i >= idx:
            dfs(n,l,i+1,t+A[i][0],k+A[i][1])

for tc in range(1,1+int(input())):
    n,l = map(int,input().split())
    A=[]
    Max_t,Max_k = 0,0
    for _ in range(n):
        t,k = map(int,input().split())
        A.append([t,k])
    dfs(n,l)
    print(f'#{tc} {Max_t}')