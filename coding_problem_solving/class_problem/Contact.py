# 마지막에 동시에 연락 받은 사람은 8번, 10번, 17번의 세 명이다.
# 이 중에서 가장 숫자가 큰 사람은 17번이므로 17을 반환하면 된다.

for i in range(1,11):
    n, st = map(int,input().split())
    lst = [list(map(int,input().split()))]
    call = [[] for _ in range(101)]
    lvl = int(n**(1/2))