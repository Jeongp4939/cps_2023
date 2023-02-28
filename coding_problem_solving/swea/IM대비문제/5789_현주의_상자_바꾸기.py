for tc in range(1,int(input())+1):

    n,q = map(int,input().split())

    lst = [0]*(n)

    for i in range(q):
        a,b = map(int,input().split())
        for j in range(a-1,b):
            lst[j]=i+1


    print(f'#{tc}',end=' ')
    print(*lst)