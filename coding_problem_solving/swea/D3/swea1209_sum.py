# 총 10개의 테스트 케이스가 주어진다.
# 배열의 크기는 100X100으로 동일하다.
# 각 행의 합은 integer 범위를 넘어가지 않는다.
# 동일한 최댓값이 있을 경우, 하나의 값만 출력한다.

for tc in range(1,11):
    input()
    max_sum = 0
    arr = [list(map(int,input().split())) for _ in range(100)]
    
    for line in arr:            # 가로 합
        max_sum=max(sum(line),max_sum)
    
    for j in range(100):        # 세로 합
        sum_3=0
        for i in range(100):
            sum_3+=arr[i][j]
        max_sum=max(max_sum,sum_3)
    
    sum_1=sum_2=0
    for i in range(100):
        sum_1+=arr[i][i]
        sum_2+=arr[i][99-i]
    max_sum=max(max_sum,sum_1,sum_2)
    
    print(f'#{tc} {max_sum}')


