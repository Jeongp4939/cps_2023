for tc in range(1,1+int(input())):

    lst = list(map(int,input().split()))
    p1=[i for i in lst[::2]]
    p2=[i for i in lst[1::2]]

    cnt1=[0]*10
    cnt2=[0]*10

    flag = 0

    for i in range(6):
        cnt1[p1[i]]+=1
        if cnt1[p1[i]]==3:
            flag=1
            print(f'#{tc} 1')
            break
        for j in range(2,10):
            if cnt1[j-2] and cnt1[j-1] and cnt1[j]:
                flag = 1
                print(f'#{tc} 1')
                break
        if flag:
            break
        cnt2[p2[i]]+=1
        if cnt2[p2[i]]==3:
            flag = 1
            print(f'#{tc} 2')
            break
        for j in range(2,10):
            if cnt2[j-2] and cnt2[j-1] and cnt2[j]:
                flag = 1
                print(f'#{tc} 2')
                break
        if flag:
            break
    if not flag:
        print(f'#{tc} 0')