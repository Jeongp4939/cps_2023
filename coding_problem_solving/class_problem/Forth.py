for tc in range(1,int(input())+1):

    commend = input().split()
    stack = []
    top = -1
    for i in commend:
        if i not in '+-/*.':
            stack.append(int(i))
            top+=1
        elif top>=0:
            if top==0 and i !='.':
                print(f'#{tc} error')
                break
            if i =='+':
                b,a = stack.pop(),stack.pop()
                stack.append(a+b)
                top-=1
            elif i=='-':
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
                top -= 1
            elif i=='/':
                b, a = stack.pop(), stack.pop()
                stack.append(a // b)
                top -= 1
            elif i=='*':
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
                top -= 1
            elif i=='.':
                result = stack.pop()
                top -= 1
                if top>0:
                    print(f'#{tc} error')
                else:
                    print(f'#{tc} {result}')