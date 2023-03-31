def dfs(n,idx=0,st=''):
    if n == L:
        cnt1 = cnt2 = 0
        for i in st:
            if i not in aeiou:
                cnt1+=1
            else: cnt2+=1
            if cnt1 >=2 and cnt2>=1:
                print(st)
                return
    for i in range(idx,C):
        dfs(n+1,i+1,st+A[i])


L,C = map(int,input().split())
A = list(input().split())
A.sort()
aeiou = ['a','e','i','o','u']
dfs(0)