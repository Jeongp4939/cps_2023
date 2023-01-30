# 첫 번째 수로 양의 정수가 주어진다.
# 두 번째 수는 양의 정수 중에서 하나를 선택한다.
# 세 번째부터 이후에 나오는 모든 수는 앞의 앞의 수에서 앞의 수를 빼서 만든다. 예를 들어, 세 번째 수는 첫 번째 수에서 두 번째 수를 뺀 것이고, 네 번째 수는 두 번째 수에서 세 번째 수를 뺀 것이다.
# 음의 정수가 만들어지면, 이 음의 정수를 버리고 더 이상 수를 만들지 않는다.


def make_num(n):
    max_d=[]
    max_n=0
    for i in range(1,n+1):
        d=[n]                           # d = [n]으로 초기화
        d.append(i)                     # 숫자 한개 선택
        for j in range(2,n*100):        # n=1일 경우 고려 못함
            if d[j-2]-d[j-1]<0:
                break
            d.append(d[j-2]-d[j-1])
        if len(d)>max_n:
            max_d=d
            max_n=len(d)
    return max_d,max_n
    
# n(3) = n(1)-n(2)
# n(2) -> 선택한 수

n=int(input())
max_d_lst, max_n = make_num(n)

print(max_n)
print(*max_d_lst)





