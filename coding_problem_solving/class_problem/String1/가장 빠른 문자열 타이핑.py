for tc in range(1,1+int(input())):
    a,b = input().split()
    a = a.replace(b,'#')

    print(f'#{tc} {len(a)}')