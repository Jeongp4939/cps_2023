# import sys
# sys.stdin = open('input.txt','r')

for tc in range(1,1+int(input())):
    
    # 암호 해석을 위한 딕셔너리 생성
    pw_dic = {'0001101':0,'0011001':1,
              '0010011':2,'0111101':3,
              '0100011':4,'0110001':5,
              '0101111':6,'0111011':7,
              '0110111':8,'0001011':9}

    n,m = map(int,input().split())
    arr = [input() for _ in range(n)]
    s= ''
    for i in arr:
        if '1' in i:
            s=i
            break
    st=0
    flag=0

    # 암호가 있는 문자열 탐색
    for i in range(len(s)-56):
        answer = []
        if s[i:i+7] in pw_dic.keys():
            ss=s[i:i+56]
            for j in range(8):
                if ss[j*7:j*7+7] in pw_dic.keys():
                    answer.append(pw_dic.get(ss[j*7:j*7+7]))
                else:
                    continue
            # 8자의 암호로 이루어진 문자열을 찾으면 break
            if len(answer)==8:
                break
    
    # 암호 판별이 성공하면 암호들의 합을 출력/아니면 0 출력 
    if not (sum(answer[::2])*3+sum(answer[1::2]))%10:
        print(f'#{tc} {sum(answer)}')
    else:
        print(f'#{tc} 0')