for tc in range(1,int(input())+1):
    n = int(input())
    nS = input()

    cnt = 0
    max_cnt = 0


    for i in nS:
        if i == '1':
            cnt +=1
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 0
    print(f'#{tc} {max_cnt}')

