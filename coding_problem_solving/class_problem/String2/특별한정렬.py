def sorting(n, arr):
    result = []
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    while arr:
        result.append(arr.pop(0))
        if arr:
            result.append(arr.pop())
    return result


for tc in range(1,int(input())+1):
    N = int(input())
    lst = list(map(int,input().split()))

    result = sorting(N,lst)

    print(f'#{tc}',*result[:10])