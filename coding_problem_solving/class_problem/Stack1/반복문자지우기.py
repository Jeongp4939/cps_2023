for tc in range(1,int(input())+1):
    s = input()
    length = len(s)
    i = 1

    while i < length:
        if s[i-1]==s[i]:
            s = s[:i-1]+s[i+1:]
            length-=2
            i=0
        i+=1

    print(f'#{tc} {len(s)}')

