# 두개의 직사각형
# 겹쳐져서 사각형이 나오면 a 직선은 b 점은 c 없으면 d
# 입력 좌표는 왼쪽 아래 x,y 오른쪽 위 p,q 순으로

for tc in range(4): # 4번 반복하는 프로그램

    x,y,p,q,x2,y2,p2,q2 = map(int,input().split())

    # 무게중심을 이용, 직사각형 무게중심==중심점
