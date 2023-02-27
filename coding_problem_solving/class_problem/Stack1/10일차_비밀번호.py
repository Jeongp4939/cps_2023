for tc in range(1,11):
    n,s = input().split()
    stack = []
    top = -1
    for i in s:
        if not stack:
            stack.append(i)
            top+=1
        elif stack[top]==i:
            stack.pop()
            top-=1
        else:
            stack.append(i)
            top+=1
    s = int(''.join(stack))

    print(f'#{tc} {s}')