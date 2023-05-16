import math

S,P = map(int,input().split())

if S==P:
    print(1)
else:
    pre = -1
    i = 2
    while 1:
        cur = math.pow(S/i,i)
        if pre>cur:
            print("-1")
            break
        if P<=cur:
            print(i)
            break
        pre = cur
        i +=1