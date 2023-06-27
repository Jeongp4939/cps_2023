import math
num = int(input())
results = []

for i in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) # 두 원의 중심 사이의 거리
    if x1 == x2 and y1 == y2 and r1 == r2: results.append(-1) # 교점이 무한대
    elif abs(r1 - r2) < d and r1 + r2 > d: results.append(2) # 교점이 두 개인 경우
    elif abs(r1 - r2) == d or r1 + r2 == d: results.append(1) # 접하는 경우
    else: results.append(0) # 교점이 없음

for result in results:
    print(result)