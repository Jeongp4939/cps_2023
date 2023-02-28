# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWS2dSgKA8MDFAVT

# 0~9 사이의 문자들로만 이루어진 문자열
# 0번 인덱스는 아무도 기립박수를 하고 있지 않을 때
# 기립박수 하고 있는 사람의 수다
# i번 째 글자가 의미하는 바는 기립 박수를 하고 있는 사람이 i-1명일 때
# 기립 박수를 하는 사람의 수를 의미???
# 문제 설명이 개떡같음..

for tc in range(1,1+int(input())):
    s = input()
    clap = int(s[0])
    cnt = 0



    print(f'#{tc} {cnt}')
