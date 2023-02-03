# 스위치 켜고 끄기 1244 S4
# 남학생 -> 스위치 번호의 배수인 스위치의 상태 변경
# 여학생 -> 자신이 받은 번호를 중심으로
# 좌우가 대칭이면서 가장 많은 스위치를 포함 하는 구간
# -> 가까운 끝에서 현재 인덱스까지의 대칭구간
# -> 이때 구간의 스위치는 항상 홀수가 된다
# 첫 줄 스위치 개수 100이하의 양의 정수
# 두번째 줄 스위치 상태
# 세번쨰 줄에 학생수 100이하의 양의 정수
# 넷재 줄부터 쭉 학생의 성별과 학생이 받은 수

Sw = int(input())    # 스위치의 개수
switch = [0]+[*map(int,input().split())]    # index 번호 맞추기
num_std = int(input())
students = [[0,0]]+[[*map(int,input().split())] for i in range(num_std)]


def set_switch(sw):                                             # 스위치 변경
    if sw:                                                      # 켜져있다면 끄고
        return 0
    return 1                                                    # 꺼져있으면 키는

for n in range(1,num_std+1):
    if students[n][0] ==1:                                      # 남자일 때 해당 번호의 배수인 스위치 상태 변경
        for i in range(1,Sw+1):
            if not i%students[n][1]:
                switch[i] = set_switch(switch[i])
    elif students[n][0] ==2:                                    # 여자 일 때 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간
        dr = min(students[n][1]-1,Sw-students[n][1])            # 양 끝 중 가까운 거리를 계산    1~idx, idx~Sw
        cnt = 0
        for i in range(dr):
            if switch[students[n][1]-i-1] == switch[students[n][1]+i+1]:
                cnt += 1
            else: break
        for i in range(students[n][1]-cnt,students[n][1]+cnt+1):
            switch[i] = set_switch(switch[i])

for i in range(len(switch[1:])//20+1):
    print(*switch[1+20*i:1+20*(i+1)])                           # 한 줄에 최대 20개 씩 출력

