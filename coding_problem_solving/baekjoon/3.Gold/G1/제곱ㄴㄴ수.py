m, M = map(int,input().split())

Set = set(i for i in range(m,M+1))
for i in range(2,int(M**0.5)+1):
    tmp = i*i
    for j in range((m//tmp)*tmp,M+1,tmp):
        if j in Set:
            Set.remove(j)
print(len(Set))

