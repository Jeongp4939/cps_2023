for tc in range(1,int(input())+1):
    n = int(input())
    divs = [2, 3, 5, 7, 11]
    n_cnt = [0] * 12
    for i in divs:
        while not n%i:
            n //= i
            n_cnt[i] += 1

    print(f'#{tc} {n_cnt[2]} {n_cnt[3]} {n_cnt[5]} {n_cnt[7]} {n_cnt[11]}')
