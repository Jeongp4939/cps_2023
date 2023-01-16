# 알파벳을 숫자로 변환
# 대문자만 입력으로 들어온다 가정

dic={}

for idx,i in enumerate(range(65,91)):
    dic[chr(i)] = idx+1

st = str(input())
for i in st:
    print(dic[i], end=' ')