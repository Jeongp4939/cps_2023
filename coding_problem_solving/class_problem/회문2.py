# import sys
# sys.stdin = open('input.txt','r')
# 100 x 100 글자판 정사각형
# 'A','B','C' 중하나가 각 위치에 들어간다
import copy
# import time
# start = time.time()
def transpose(ar):          # 전치행렬 생성 함수
    new_ar = copy.deepcopy(ar)

    for i in range(100):
        for j in range(i,100):
            new_ar[i][j],new_ar[j][i] = new_ar[j][i],new_ar[i][j]

    return new_ar


def is_palindrome(line,n):     # 회문 검사 함수
    if n==100:
        if line == line[::-1]:
            return n
    else:
        for i in range(101-n):
            s = line[i:i+n]
            if s == s[::-1]:
                return n
    return 0


for tc in range(1,11):
    input()

    arr = [list(input()) for _ in range(100)]
    arr_trans = transpose(arr)  # 세로 회문 검사를 위한 전치행렬

    max_len = 1         # 문자 한개도 회문이므로 1로 시작
    pal1 = 1            # arr 내부 회문의 길이
    pal2 = 1            # arr_trans 내부 회문의 길이

    for i in range(100):
        for j in range(1,101):
            pal1 = is_palindrome(arr[i], j)
            pal2 = is_palindrome(arr_trans[i], j)
            if pal1>max_len:
                max_len = pal1
            if pal2>max_len:
                max_len = pal2

    print(f'#{tc} {max_len}')

# end = time.time()
# print(end-start)