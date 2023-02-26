# https://www.acmicpc.net/problem/1018

def check(a,b):
    cnt1=cnt2=0
    for i in range(8):
        for j in range(8):
            if (i+j)%2 and arr[a+i][b+j]=='W':
                cnt1+=1
            elif not (i+j)%2 and arr[a+i][b+j]=='B':
                cnt1+=1
    for i in range(8):
        for j in range(8):
            if (i+j)%2 and arr[a+i][b+j]=='B':
                cnt2+=1
            elif not (i+j)%2 and arr[a+i][b+j]=='W':
                cnt2+=1
    return min(cnt1,cnt2)

n, m = map(int,input().split())
arr=[list(input()) for _ in range(n)]
Min = n*m

for i in range(0,n-7):
    for j in range(0,m-7):
        cnt=check(i,j)
        if Min>cnt:
            Min=cnt

print(Min)