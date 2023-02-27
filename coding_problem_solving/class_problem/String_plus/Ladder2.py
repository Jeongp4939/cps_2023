import sys
sys.stdin = open('../input.txt', 'r')
import copy

dy,dx = [1,0,0],[0,-1,1]

def ladder(ar,x,y=0):
    new_ar = copy.deepcopy(ar)
    start = []
    start.append([y,x])

    cnt = 0

    while start:
        y, x = start.pop()

        for i in range(1,3):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0<=ny<100 and 0<=nx<100 and new_ar[ny][nx]:
                if ny==99:
                    return cnt
                new_ar[ny][nx]=0
                start.append([ny,nx])
                cnt+=1
                break

        else:
            ny = y+dy[0]
            nx = x+dx[0]

            if 0<=ny<100 and 0<=nx<100 and new_ar[ny][nx]:
                if ny==99:
                    return cnt
                new_ar[ny][nx]=0
                start.append([ny,nx])
                cnt+=1
    return 0

for tc in range(1,11):
    input()
    arr = [list(map(int,input().split())) for _ in range(100)]
    result = 10**10
    for i in range(100):
        if arr[0][i]==1 and ladder(arr,i):
            if result > ladder(arr,i):
                result = ladder(arr,i)
                result_x = i
    print(f'#{tc} {result_x}')
