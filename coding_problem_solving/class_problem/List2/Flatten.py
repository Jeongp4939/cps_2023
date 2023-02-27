# 가장 높은 곳의 블럭을 가장 낮은곳으로 옮기는걸 평탄화
def lst_min_max(lst):
    mx_n=mn_n = lst[0]
    max_n_idx=min_n_idx=0
    for i in lst:
        if i < mn_n:
            mn_n = i
            min_n_idx=lst.index(i)
        if i > mx_n:
            mx_n = i
            max_n_idx = lst.index(i)
    return mn_n,min_n_idx,mx_n,max_n_idx

for tc in range(1,11):
    dump = int(input())
    g = list(map(int,input().split()))

    while dump:                  # dump가 0이 될때까지
        _, min_idx, _, max_idx = lst_min_max(g)
        if g[min_idx]==g[max_idx] or g[max_idx]-g[min_idx]==1:
            break
        dump -= 1
        g[max_idx],g[min_idx] = g[max_idx]-1,g[min_idx]+1

    mn_n, _, mx_n, _ = lst_min_max(g)
    print(f'#{tc} {mx_n-mn_n}')