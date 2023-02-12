# 지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
# 지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
# 지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
# 지붕의 가장자리는 땅에 닿아야 한다.
# 비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.

# 첫 인덱스와 끝 인덱스, 최고점 인덱스를 검색
# 밖에 있는 기둥이 더 낮으면 한단계 높은 기둥까지 연결
# 밖에 있는 기둥보다 안에 있는 기둥이 낮으면
# 더 높은 기둥이 나올때까지 진행

N = int(input())
lst_height = [0]*1001

for _ in range(N):      # 기둥 높이 배열 생성
    idx, height = map(int,input().split())
    lst_height[idx] = height

start = 0
end = 0
for i in range(1001):           # 시작 기둥 파악
    if lst_height[i]!=0:
        start = i
        break
for i in range(1000,-1,-1):     # 끝 기둥 파악
    if lst_height[i]!=0:
        end = i
        break
lst_height = lst_height[:end+2]
max_height = max(lst_height)
max_idx = lst_height.index(max_height)
height = lst_height[0]

h_lst = []

for i in range(max_idx+1):
    if lst_height[i]<=height:
        h_lst.append(height)
    if lst_height[i]> height:
        height=lst_height[i]
        h_lst.append(height)
height = lst_height[-1]
for i in range(end,max_idx,-1):
    if lst_height[i]<=height:
        h_lst.append(height)
    if lst_height[i]> height:
        height=lst_height[i]
        h_lst.append(height)
print(sum(h_lst))
cd