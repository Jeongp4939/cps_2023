import sys
sys.stdin = open('../input.txt', 'r')

for tc in range(1,1+int(input())):
    num_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    dic = {}
    for i in num_lst:
        dic[i] = 0
    n = input(f'#{tc} ')
    lst = input().split()
    for i in lst:
        dic[i]+=1
    result = ''
    for v in dic.keys():
        for _ in range(dic[v]):
            result = result + v + ' '

    print(f'#{tc}')
    print(result)
