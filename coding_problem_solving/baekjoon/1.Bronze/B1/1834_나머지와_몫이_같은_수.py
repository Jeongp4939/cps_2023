# N으로 나누었을 때 나머지와 몫이 같은 모든 자연수의 합을 구하는 프로그램을 작성하시오
# N의 크기는 2,000,000 이하의 자연수
n = int(input())
i = 1

result = 0
while i<n:
    result += n*i+i
    i+=1

print(result)

