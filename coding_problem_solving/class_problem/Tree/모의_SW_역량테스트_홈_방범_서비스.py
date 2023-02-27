# 운영 비용 = k**2+(k-1)**2
# N*N 배열에서 마름모꼴 형태 출력
# -k<=a<=k

def search(y,x,k):
    cnt = 0
    price = k**2+(k-1)**2
    for i in range(-k, k + 1):
        for j in range(-k, k + 1):
            if abs(i) + abs(j) < k and 0<=y+i<N and 0<=x+j<N:
                if arr[y + i][x + j] == 1:
                    cnt+=1
    return price, cnt

for tc in range(1,1+int(input())):
    N,n =map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    Max = 0

    for k in range(N+2):
        for i in range(N):
            for j in range(N):
                price,cnt = search(i,j,k)
                if cnt>Max and price <= cnt*n:
                    Max=cnt

    print(f'#{tc} {Max}')
