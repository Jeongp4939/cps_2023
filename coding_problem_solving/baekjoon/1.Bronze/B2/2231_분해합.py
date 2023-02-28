# https://www.acmicpc.net/problem/2231

n=int(input())
flag = 0
maker = 0
for i in range(n):
    Sum = i
    st = str(i)
    for s in st:
        Sum+=int(s)
    if Sum==n:
        flag=1
        maker=i
        break
if flag:
    print(maker)
else:
    print(0)

