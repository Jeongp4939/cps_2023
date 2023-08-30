n = int(input())
d = [0]*(n+1)
d[0]=2
for i in range(1,n+1):
  d[i] = d[i-1]*2-1
print(d[n]**2)
