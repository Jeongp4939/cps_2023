# 중간값 구하기
result = None
n = int(input())
num_li = sorted(list(map(int,input().split())))

result = num_li[n//2]

print(result)