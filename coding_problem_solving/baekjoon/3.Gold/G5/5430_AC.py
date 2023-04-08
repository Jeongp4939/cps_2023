# reverse 를 명령어가 나올 때마다 사용해서 시간초과가 나왔다
# R 명령어가 들어왔을 때 홀수번 들어오면 q의 뒤에서 꺼내고
# 짝수번 들어오면 원래 배열이므로 popleft를 하는식으로 해결

from collections import deque
T = int(input())

for tc in range(T):
    flag = 1
    result = 0
    cmd = input()
    n = int(input())
    q = deque()
    arr = input()[1:-1].split(',')
    for i in arr:
        if i.isnumeric():
            q.append(i)
    rev = 0
    for i in cmd:
        if i=='R':
            if q:
                rev+=1
        if i=='D':
            if q:
                if rev%2:
                    q.pop()
                else:
                    q.popleft()
            else:
                flag = 0
                print('error')
                break
    if flag:
        if rev%2:
            q.reverse()
            print("["+','.join(q)+"]")
        else:
            print("["+','.join(q)+"]")
