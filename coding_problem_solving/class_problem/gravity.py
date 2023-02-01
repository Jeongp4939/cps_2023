T = int(input())

for tc in range(1,T+1):
    n = int(input())
    boxes = list(map(int, input().split()))
    max_drop = 0
    for i in range(n):
        drop = 0
        for j in range(i+1,n):
            if boxes[i]>boxes[j]:
                drop += 1
        if drop > max_drop:
            max_drop=drop

    print(f'#{tc} {max_drop}')