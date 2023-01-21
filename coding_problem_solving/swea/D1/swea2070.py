# 두 수를 비교하여 부호 출력하기
T = int(input())

for tc in range(1,T+1):
    result =''

    a, b = map(int,input().split())

    if a>b:
        result = '>'
    elif a<b:
        result = '<'
    else:
        result = '='

    print(f'#{tc} {result}')