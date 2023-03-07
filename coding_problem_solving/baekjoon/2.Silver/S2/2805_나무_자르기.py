# https://www.acmicpc.net/problem/2805
# 참고 : https://data-flower.tistory.com/99

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tree = list(map(int,input().split()))
st=0
ed = max(tree)

while st<=ed:
    mid = (st+ed)//2
    Sum = 0
    for i in tree:
        if i >=mid:
            Sum += i-mid
    # 이분탐색
    if Sum >=m:
        st = mid+1
    else:
        ed = mid-1
print(ed)