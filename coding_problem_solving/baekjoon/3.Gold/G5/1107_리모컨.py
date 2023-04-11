def dfs(n_len, target, N=0):
    global Min,t_len
    # target 이 100이라면 바로 종료
    if target==100:
        Min =0
        return
    # target과 일치하는 수가 나온다면 해당 수의 자리수
    if n_len:
        if N == target:
            Min = min(Min,t_len)
            return
        else:
            Min = min(Min, n_len+abs(target-N))
    if n_len>t_len:
        return
    for i in btn:
        dfs(n_len+1,target,N*10+i)

target = int(input())
t_len = len(str(target))
n = int(input())
btn = list(range(10))
if n:
    broken = list(map(int,input().split()))
    for i in broken:
        btn.remove(i)

Min = abs(target-100)
dfs(0,target)
print(Min)
