is_prime=[0,0]+[1]*999
for i in range(len(is_prime)):
    if is_prime[i]:
        for j in range(i*2,1001,i):
            is_prime[j] = False
prime=[]
for i in range(len(is_prime)):
    if is_prime[i]:
        prime.append(i)
# print(prime)

cnt = 0
N = input()
N_lst = list(map(int,input().split()))
for i in N_lst:
    if i in prime:
        cnt+=1
print(cnt)
