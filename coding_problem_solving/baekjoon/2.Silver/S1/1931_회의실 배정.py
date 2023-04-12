N = int(input())
lst = []
for i in range(N):
    a,b = map(int,input().split())
    lst.append((a,b))

lst = sorted(lst,key=lambda x:(x[1],x[0]))
ed = lst[0][1]
cnt = 1
for i in range(1,N):
    if ed <= lst[i][0]:
        ed = lst[i][1]
        cnt+=1
print(cnt)
