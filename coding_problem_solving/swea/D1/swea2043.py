# 비밀번호 맞추기(입력 수부터 비밀번호까지의 횟수)

P, K = map(int, input().split())

if P >= K:
    print(P-K+1)
else:
    print(P+1000-K)
