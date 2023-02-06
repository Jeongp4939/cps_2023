def bingo(arr):
    bingo_ = 0
    sum_ = 0
    for i in range(5):
        if sum(arr[i]) == 0:
            bingo_+=1

    for i in range(5):
        for j in range(5):
            sum_+=arr[j][i]
        if sum_ ==0:
            bingo_+=1
        sum_ = 0

    for i in range(5):
        sum_ += arr[i][i]
    if sum_ ==0:
        bingo_+=1
    sum_ = 0

    for i in range(5):
        sum_ += arr[i][4-i]
    if sum_ ==0:
        bingo_+=1
    return bingo_ >= 3


def bingo_check(arr,n):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == n:
                arr[i][j] = 0

b_map = [list(map(int, input().split())) for _ in range(5)]
arr = []
for i in range(5):      # arr을 1차원 배열로
    arr += list(map(int,input().split()))

cnt=0

for k in arr:
    bingo_check(b_map,k)
    cnt+=1
    if bingo(b_map):
        break

print(cnt)


