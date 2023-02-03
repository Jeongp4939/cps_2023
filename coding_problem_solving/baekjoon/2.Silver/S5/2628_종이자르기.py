# 실버 5
# 종이 자르기

# 입력 형식
# 가로 세로
# 자를 수
# 0(가로로 컷)/1(세로로 컷) + 번호

x, y = map(int,input().split())
n = int(input())
hor = [0, y]   # 종이의 최대 크기
ver = [0, x]   # 종이의 최대 크기
for _ in range(n):

    d, line = map(int,input().split())
    if d == 0:
        hor.append(line)
    elif d == 1:
        ver.append(line)
    max_h = max_v = 0
    temp = 0
    hor.sort()
    ver.sort()
    for i in range(1,len(hor)):
        temp = hor[i]-hor[i-1]
        if max_h<temp:
            max_h = temp
    for i in range(1,len(ver)):
        temp = ver[i]-ver[i-1]
        if max_v<temp:
            max_v = temp
print(max_v*max_h)