# https://www.acmicpc.net/problem/2108
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.

# def m(ar,n):
#     Sum = sum(ar)
#     Sum/=n
#     if (Sum>=0 and (Sum*10)%10<5) or (Sum<0 and 10-(Sum*10)%10<5):
#         Sum = int(Sum)
#     else:
#         if Sum>=0:
#             Sum = int(Sum)+1
#         else:
#             Sum = int(Sum)-1
#     return Sum

import sys
input = sys.stdin.readline

def most(ar):
    dic = {}
    for i in ar:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    tmp = []
    Max = dic[0][1]
    for i in dic:
        if i[1]==Max:
            tmp.append(i[0])
    tmp.sort()
    if len(tmp)>=2:
        return tmp[1]
    else:
        return tmp[0]

n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))
lst = sorted(lst)

print(round(sum(lst)/n))
print(lst[n//2])
print(most(lst))
print(lst[-1]-lst[0])





