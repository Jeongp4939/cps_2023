# https://www.acmicpc.net/problem/2292
# 1 : 1, 2~7: 2, 8~ 19: 3, 20~37 : 4
# 1->1, 2~7-> 6, 8~19->12


n = int(input())
cnt = 1

if n==1:
    print(1)
else:
    i = 1
    max_c = 1
    while 1:
        if max_c>=n:
            print(cnt)
            break
        max_c+=6*i
        cnt+=1
        i+=1