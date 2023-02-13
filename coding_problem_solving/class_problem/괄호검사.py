for tc in range(1,int(input())+1):

    s = input()

    stack = []
    top = -1

    for i in s:
        if not stack:
            if i in ['(',')','{','}','[',']']:
                stack.append(i)
                top+=1
        else:
            if i in ['(', ')', '{', '}', '[', ']']:
                if stack[top]=='(' and i==')':
                    stack.pop()
                    top-=1
                elif stack[top]=='{' and i=='}':
                    stack.pop()
                    top-=1
                elif stack[top]=='[' and i==']':
                    stack.pop()
                    top-=1
                else:
                    stack.append(i)
                    top+=1
    if stack:
        print(f'#{tc}',0)
    else:
        print(f'#{tc}',1)