while 1:
    flag = 1
    stack = []
    a = input()
    if a == '.':
        break
    for i in a:
        if i in ['(','[']:
            stack.append(i)
        elif i in [')',']']:
            if not stack:
                flag=0
                break
            if i ==')' and stack[-1]=='(':
                stack.pop()
            elif i == ']' and stack[-1]=='[':
                stack.pop()
            else:
                flag=0
    if stack:
        flag=0
    if flag:
        print('yes')
    else:
        print('no')

