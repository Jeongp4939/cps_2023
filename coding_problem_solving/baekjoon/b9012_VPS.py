# 입력 데이터는 표준 입력을 사용한다.입력은 T개의 테스트 데이터로 주어진다.
# 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
# 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다.
# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
# 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)
# fail
import sys

for _ in range(int(sys.stdin.readline())):
    PS=sys.stdin.readline().rstrip()
    if len(PS)&1:
        print('NO')
        continue

    lcnt = 0
    rcnt = 0



    if PS[0]==')' or PS[-1]=='(':
        print('NO')
        continue

    for i in PS:
        break_flag = True
        if i =='(':
            lcnt+=1
        else:
            rcnt+=1
        if rcnt > lcnt:
            print('NO')
            break_flag=False
            break
    if break_flag==False:
        break
    if lcnt==rcnt:
        print('YES')
    else:
        print('NO')