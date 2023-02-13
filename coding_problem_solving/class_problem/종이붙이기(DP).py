# 가로길이가 n이 되게하는 모든 조합의 수
# 가로길이는 20*10 에서 10, 20
# 20*20 에서 20
# 총 세 경우

for tc in range(1,int(input())+1):
    n = int(input())//10
    D = [0]*31
    D[1],D[2] = 1, 3
    for i in range(3,31):
        D[i] = D[i-1]*2-1 if i%2 else D[i-1]*2+1
    print(f'#{tc} {D[n]}')