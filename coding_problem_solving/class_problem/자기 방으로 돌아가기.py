# 테스트 케이스
# N 돌아가야 할 학생들의 수
# 현재방, 돌아갈 방으로 구성
# 가는 경로가 겹치면 기다려야함
# 홀수 짝수번 방이 복도를 공유
# (방번호-1)//2 : 복도 번호

for tc in range(1,int(input())+1):
    n = int(input())
    cnts = [0]*400                  # 복도
    for _ in range(n):      # 학생 배열 구성
        a,b = map(int,input().split())
        if a<b:
            for j in range((a-1)//2,(b-1)//2+1):
                cnts[j]+=1
        else:
            for j in range((b-1)//2,(a-1)//2+1):
                cnts[j]+=1
    print(f'#{tc} {max(cnts)}')


