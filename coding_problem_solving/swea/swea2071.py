T = int(input())

for tc in range(1,T+1):
    n_li = list(map(int,input().split()))
    m = 0
    li_sum = sum(n_li)
    if li_sum%10 >= 5:
        m = li_sum//10 + 1
    else:
        m = li_sum//10

    print(f'#{tc} {m}')