# 최대수 구하기
T = int(input())

for tc in range(1,T+1):

    num_li = list(map(int,input().split()))
    
    result = sorted(num_li, reverse=True)[0]

    print(f'#{tc} {result}')