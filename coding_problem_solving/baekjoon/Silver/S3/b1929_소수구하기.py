is_prime=[0,0]+[1]*1000000
for i in range(2,1000000):
    if is_prime[i]:
        for j in range(i*2,1000001,i):
            is_prime[j] = False
        
m,n = map(int,input().split())
for i in range(m,n+1):
    if is_prime[i]:
        print(i)