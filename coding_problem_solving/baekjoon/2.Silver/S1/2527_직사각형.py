# 두개의 직사각형
# 겹쳐져서 사각형이 나오면 a 직선은 b 점은 c 없으면 d
# 입력 좌표는 왼쪽 아래 x,y 오른쪽 위 p,q 순으로

def rect(x1, y1, p1, q1, x2, y2, p2, q2):
    # 1. 안만나는 경우
    if (x2>p1) or (x1>p2) or (y1>q2) or (y2>q1):
        print('d')
        return
    # 2. 한 점에서 만나는 경우
    if (x1==p2 and (y1==q2 or q1==y2)) or (p1==x2 and (y1==q2 or q1==y2)):
        print('c')
        return
    # 3. 선분이 만나는 경우
    if x1==p2 or x2==p1 or y1==q2 or y2==q1:
        print('b')
        return
    # 4. 나머지 겹치는 경우
    print('a')
    return

# 총 4번의 테스트 케이스
for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())     # 직사각형의 좌표값 입력
    rect(x1, y1, p1, q1, x2, y2, p2, q2)