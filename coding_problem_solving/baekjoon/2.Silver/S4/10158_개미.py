# 가로 w, 세로 h
# 개미 -> 오른쪽 위 45도 방향으로 일정한 속력 이동
# 부딪히면 입사각 반사각에 입각하여 이동
# 2<=w,h <= 40,000
# p,q 는 w,h 안쪽에 설정
# 1<=t<=200,000,000

w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())

if not ((p+t)//w)%2:    # 짝수 일 때 -> 정방향
    p_idx = (p+t)%w
else:                   # 홀수 일 때 -> 역방향
    p_idx = w- (p + t) % w
if not ((q+t)//h)%2:
    q_idx = (q+t)%h
else:
    q_idx = h- (q + t) % h

print(p_idx,q_idx)

