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
# N의 범위가 1~1000이므로 기둥의 빈 배열 생성
lst_height = [0]*1001

for _ in range(N):      # 기둥 높이 배열 생성
    idx, height = map(int,input().split())
    lst_height[idx] = height

start = 0
end = 0

# 첫 인덱스부터 뒤로 검색, 기둥을 만나면 정지
for i in range(1001):           # 시작 기둥 파악
    if lst_height[i]!=0:
        start = i
        break
# 끝 인덱스부터 앞으로 검색, 기둥을 만나면 정지
for i in range(1000,-1,-1):     # 끝 기둥 파악
    if lst_height[i]!=0:
        end = i
        break

# 기둥이 있는 부분의 리스트만 따로 분리
lst_height = lst_height[:end+2]

# 가장 높은 기둥의 높이와 그 인덱스 저장
max_height = max(lst_height)
max_idx = lst_height.index(max_height)

# 현재 높이는 0번 인덱스의 높이
height = lst_height[0]

# 천장의 높이를 저장하는 배열 생성
h_lst = []

# 앞에서부터 높이가 가장 높은 인덱스까지 진행
# 현재 인덱스의 높이가 저장된 높이보다 낮으면 인덱스의 높이를 저장
for i in range(max_idx+1):
    if lst_height[i]<=height:
        h_lst.append(height)
    # 현재 인덱스의 높이가 높으면 현재 높이를 저장하고, height을 현재값으로 초기화
    if lst_height[i]> height:
        height=lst_height[i]
        h_lst.append(height)

# 다음 검색을 위해 인덱스를 끝 인덱스로 변경
height = lst_height[-1]
# 위와 같은 과정을 반복(가장 높은 기둥의 바로 앞 인덱스까지)
for i in range(end,max_idx,-1):
    if lst_height[i]<=height:
        h_lst.append(height)
    if lst_height[i]> height:
        height=lst_height[i]
        h_lst.append(height)
print(sum(h_lst))
