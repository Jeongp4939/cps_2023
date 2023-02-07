# n명의 사람, m초의 시간에 k개의 붕어빵
# lst 에는 사람이 도착하는 시간

for tc in range(1, int(input())+1):
    n,m,k = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort()
    second = 0
    bread = 0
    # i번째 사람이 도착할 때까지의 빵의 개수 (lst[i]//m)*k
    for i in range(len(lst)):
        second = lst[i]
        bread = (second//m)*k-i-1
        if bread<0:
            print(f'#{tc} Impossible')
            break
    else:
        print(f'#{tc} Possible')