T = int(input())

for tc in range(1,T+1):
    N = int(input())
    n=input()
    res=[0]*100
    max_n = 0
    max_n_idx=0
    for i in n:
        res[int(i)]+=1
    for i in res:
        if i > max_n:
            max_n=i
    for idx in range(100):
        if res[idx]==max_n:
            max_n_idx = idx
    print(f'#{tc} {max_n_idx} {max_n}')

