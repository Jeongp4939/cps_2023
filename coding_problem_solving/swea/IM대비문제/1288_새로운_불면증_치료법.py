# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18_yw6I9MCFAZN

for tc in range(1,1+int(input())):
    used=[0]*10
    n = int(input())
    new_n=n
    cnt = 0

    while 0 in used:
        for i in str(new_n):
            used[int(i)]=1
        cnt+=1
        new_n+=n

    print(f'#{tc} {new_n-n}')