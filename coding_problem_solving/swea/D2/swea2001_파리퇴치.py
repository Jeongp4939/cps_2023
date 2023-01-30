T = int(input())

# M x M 합하기
def sum_area(map_arr,y,x,M):
    rlt=0
    for i in range(y,y+M):
        for j in range(x,x+M):
            rlt+=map_arr[i][j]
    return rlt

for tc in range(1,T+1):
    # N x N 배열, M x M 크기로 합하기
    N ,M = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]
    max_result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            result = sum_area(arr,i,j,M)
            max_result = max(result,max_result)
    

    print(f'#{tc} {max_result}')