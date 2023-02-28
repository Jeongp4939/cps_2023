# https://www.acmicpc.net/problem/2609

def gcd(a,b):
    if a%b == 0:
        return b
    elif b%a==0:
        return a
    else:
        cd=1
        for i in range(1,min(a,b)//2+1):
            if a%i==b%i==0:
                cd=i
        return cd
def lcm(a,b):
    return (a*b)//gcd(a,b)

a,b = map(int,input().split())
print(gcd(a,b))
print(lcm(a,b))

