# 몫과 나머지 출력

T = int(input())

for tc in range(1,T+1):
    a, b = map(int, input().split())
    print(f'#{tc} {a//b} {a%b}')