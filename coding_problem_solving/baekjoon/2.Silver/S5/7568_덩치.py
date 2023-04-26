N = int(input())
lst = []
rlt = [1]*N
for i in range(N):
    w,h = map(int,input().split())
    lst.append((w,h))

for i in range(N):
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            rlt[i]+=1

print(*rlt)