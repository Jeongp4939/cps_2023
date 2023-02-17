# 쌓여있는 막대기의 수 cnt
# '(' cnt+=1 -> 레이저 시작(?)
#  뒤를 체크(범위!)-> 앞을 체크 -> index 사용
# else ')'
# if st[i-1] == '('  # 레이저
#           cnt -= 1, ans+=cnt
# else # ')' 막대기 끝
#           cnt-=1, ans+=1

for tc in range(1,int(input())+1):

    st = input()
    ans = cnt = 0
    for i in range(len(st)):
        if st[i] == '(':
            cnt += 1
        else:           # ')'
            if st[i-1]=='(':
                cnt-=1
                ans+=cnt
            else:
                cnt-=1
                ans+=1

    print(f'#{tc} {ans}')
