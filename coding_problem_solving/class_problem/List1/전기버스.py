T = int(input())

for tc in range(1,T+1):
    # K 갈 수 있는 거리, N 총 정거장 수, M 충전기 설치 수
    K,N,M = map(int,input().split())
    # 충전기가 설치된 정류장 리스트
    charge_machine = list(map(int,input().split()))

    bus_stop = [0]*(N+1)
    # 빈 정류장 배열 만들기 0번 부터 N번 정류장까지 존재->n+1개의 정류장
    charge = 0
    # 충전기가 설치된 정류장 번호에 1로 존재여부 표기
    for i in charge_machine:
        bus_stop[i]=1

    # 현재 정거장에서 K 거리 밖의 정거장 사이에 충전기가 있는지 확인 K 범위->1~K -> range(K,0,-1)
    # 범위 안에 충전기가 없으면 끝내고 0을 출력
    # 충전기가 존재하면 해당 정류장으로 이동
    # 종점에 도달할 수 있는 위치의 충전기가 있는 정류장에 도착하면 끝내고 횟수를 출력하고 끝
    # while-for, flag 를 이용해 다중 반복문 탈출
    flag = False
    i=0

    while i < N:
        if 1 in bus_stop[i:]:
            for j in range(K,0,-1):
                if i+j >= N:
                    break
                if bus_stop[i+j]==1:    # 범위 중 먼 거리에 충전기가 있으면 이동, 충전
                    charge+=1
                    i=i+j-1
                    break
            else:           # for문에서 break가 실행 안되면 실행
                flag = True   # flag를 세우고 0을 출력하고 탈출
                print(f'#{tc} {0}')
                break
        i+=1
    if not flag:
        print(f'#{tc} {charge}')





