import sys
sys.stdin = open('input.txt','r')

def isPel(arr,m):
    for i in range(len(arr)):
        if len(arr[i])==m:
            if arr[i] == arr[i][::-1]:
                    return ''.join(arr[i])
        else:
            for j in range(len(arr[i])-m+1):
                s = ''.join(arr[i][j:j+m])
                if s == s[::-1]:
                    return s


for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    s_lst = [list(input()) for i in range(n)]
    s_lst_trans = [[' ']*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s_lst_trans[j][i] = s_lst[i][j]
    result =''
    result = isPel(s_lst,m) if isPel(s_lst,m) else isPel(s_lst_trans,m)

    print(f'#{tc} {result}')
