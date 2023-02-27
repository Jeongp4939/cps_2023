
def inorder(n=1):
    if n>=N+1:
        return
    inorder(n*2)
    if n<N+1:
        print(arr[n][0],end='')
    inorder(n*2+1)

T = 10
for tc in range(1,1+T):
    N = int(input())
    arr=[[]for _ in range(N+1)]
    for _ in range(N):
        i, node, *args = input().split()
        arr[int(i)].append(node)

    print(f'#{tc}',end=' ')
    inorder()
    print()