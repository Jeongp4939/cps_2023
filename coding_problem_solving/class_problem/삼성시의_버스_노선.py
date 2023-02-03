# 5000개의 버스 정류장(1~5000번)
# T케이스 주어짐
# 각 케이스 첫번 째 줄 N(1~500)
# i번째 줄 두 정수 Ai,Bi 가 공백으로 구분
# 다음 줄에 하나의 정수 P(1~500)
# 다음 P개의 줄 j번쨰 줄 정수 Cj(1~5000)
# 빈도수 배열 cnts[] 생성

# import sys
# sys.stdin = open("input.txt","r")

for tc in range(1,1+int(input())):
    n = int(input())

    cnts = [0]*5001

    for _ in range(n):
        S, E = map(int,input().split())
        for i in range(S, E+1):
            cnts[i]+=1
    P = int(input())
    alst = []
    for _ in range(P):
        p = int(input())
        alst.append(cnts[p])
    print(f'#{tc}', *alst)
