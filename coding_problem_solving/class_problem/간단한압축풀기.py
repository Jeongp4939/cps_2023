for tc in range(1,1+int(input())):
    n = int(input())
    dic = {}
    for _ in range(n):
        a,b = input().split()
        dic[a]=int(b)
    cnt = 0
    print(f'#{tc}')
    for i in dic.keys():
        while dic[i]!=0:
            print(i,end='')
            dic[i]-=1
            cnt+=1
            if cnt == 10:
                print()
                cnt = 0
    print()