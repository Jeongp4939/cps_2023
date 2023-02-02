# 이진 탐색
# 정렬된 상태에서 사용 해야함
# mid = (start + end) // 2
# mid 가 target 과 일치할 때까지 반복
# mid 가 target 보다 크면 end 작으면 start 이동
# mid 가 target 과 같아질 때까지 반복
# mid 가 target 보다 크면 end=mid-1
# mid 가 target 보다 작으면 start=mid-1

def binary_search(start, target, end):
    cnt = 0

    while True:
        mid = (start + end) // 2
        if mid == target:
            return cnt
        elif mid > target:
            end = mid
            cnt += 1
        else:
            start = mid
            cnt += 1

for tc in range(1, int(input()) + 1):
    n, a, b = map(int, input().split())
    if binary_search(1, a, n) < binary_search(1, b, n):
        print(f'#{tc} A')
    elif binary_search(1, a, n) > binary_search(1, b, n):
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
