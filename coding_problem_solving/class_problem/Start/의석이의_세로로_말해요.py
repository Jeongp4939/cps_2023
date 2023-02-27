for tc in range(1,1+int(input())):
    arr=[input() for _ in range(5)]
    Max_len = 0
    for i in arr:
        if len(i)>Max_len:
            Max_len=len(i)

    for i in range(5):
        while len(arr[i])<Max_len:
            arr[i]+=' '
    arr_t = map(list,zip(*arr))
    rlt=''
    for i in arr_t:
        for j in i:
            if j==' ':
                continue
            else:
                rlt+=j
    print(f'#{tc} {rlt}')
