def is_pal(s):
    if s==s[::-1]:
        return s
    return False

def transpose(ar):
    new_ar = [[0]*len(ar) for _ in range(len(ar[0]))]

    for i in range(len(ar)):
        for j in range(len(ar[0])):
            ar[i][j] = new_ar[j][i]

    return new_ar





for _ in range(1,11):
    tc = input()

    arr = [list(input()) for _ in range(100)]
    arr_trans= transpose(arr)






