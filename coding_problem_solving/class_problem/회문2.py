def is_pal(s):
    if s==s[::-1]:
        return s
    return False


for _ in range(1,11):
    tc = input()

    arr = [list(input()) for _ in range(100)]
    arr_trans=[[0]*100 for _ in range(100)]

    max_pal_len = 0


    for i in range(arr):
        for j in range(arr):
            arr_trans[i][j] = arr[j][i]



