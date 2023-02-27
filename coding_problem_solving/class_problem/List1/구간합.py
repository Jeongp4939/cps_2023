T = int(input())

for tc in range(1,T+1):
    n,m = map(int,input().split())
    numbers = list(map(int,input().split()))
    result_max = 0
    result_min = 10**10

    for i in range(n-m+1):
        sum = 0
        for j in range(m):
            sum+=numbers[i+j]
        if sum>result_max:
            result_max=sum
        if sum<result_min:
            result_min=sum

    print(f'#{tc} {result_max-result_min}')