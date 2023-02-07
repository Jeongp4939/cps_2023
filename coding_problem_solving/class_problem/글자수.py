for tc in range(1,int(input())+1):
    s1 = input()
    s2 = input()
    dic = {}
    for i in s1:
        dic[i]=0

    for i in s2:
        if i in dic:
            dic[i]+=1

    dic_values = sorted(dic.values(),reverse=True)

    print(f'#{tc} {dic_values[0]}')
