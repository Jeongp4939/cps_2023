prime = set(range(2,10001))

for i in range(2,10001):
    for j in range(2,10001//i+1):
        if i*j in prime:
            prime.remove(i*j)

prime = sorted(list(prime))

n = int(input())
m = int(input())

sub_prime = [i for i in prime if n <= i <= m]

if len(sub_prime)!=0:
    print(sum(sub_prime))
    print(sub_prime[0])
else:
    print(-1)
