def multiple(a,b):
    if b==0:
        return 1
    return a*multiple(a,b-1)

for tc in range(1,11):
    input()
    a,b = map(int,input().split())
    print(f'#{tc} {multiple(a,b)}')
