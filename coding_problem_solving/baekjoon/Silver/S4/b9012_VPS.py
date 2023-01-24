# 입력 데이터는 표준 입력을 사용한다.입력은 T개의 테스트 데이터로 주어진다.
# 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
# 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다.
# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
# 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)
# fail
import sys

def input():    # 입력 방식 sys를 이용한 방법으로 변경
    return sys.stdin.readline().rstrip()

N = int(input())
result = ''

for _ in range(N):
    testcase = input()
    cnt = 0
    for c in testcase:      # for - else for 문
        if c=='(':          # 시작이 (가 아니면 바로 NO
            cnt+=1
        else:
            cnt-=1
        if cnt < 0:         # 시작이 ) 이거나 )의 개수가 더 많음
            result += "NO\n"
            break
    else:                   # for - else else 문
        if cnt==0:          # 문제 없이 ( ) 개수가 같으면 yes
            result+="YES\n"
        else:               # 개수가 다르면 () 를 완성할 수 없으므로 no
            result+="NO\n"

print(result)