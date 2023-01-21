# 미로1
dx = [0,0,1,-1]   # 상하좌우 방향
dy = [1,-1,0,0]

def wall_ex(x, y, n=16):
    if x<0 or y<0 or x>=n or y>=n:
        return True
    return False

for tc in range(1,10):
    T = int(input())
    arr = []
    for _ in range(16):
        arr.append(list(map(int,input())))

