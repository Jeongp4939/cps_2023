# 1. postorder의 마지막 node가 root node
# 2. root를 기준으로 inorder와 postorder의 좌우 노드의 수는 같음을 이용
# 3. root를 기준으로 왼쪽과 오른쪽 노드의 수를 계산
# 4. 인덱스를 기반으로 1~3을 반복
# 5. 왼쪽부터 root에 해당하는 노드를 출력하면 preorder가 완성

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def order(i_start, i_end, p_start, p_end):
    if (p_start > p_end) or (i_start>i_end):
        return
    root = postorder[p_end]
    left_len = indexes[root] - i_start
    right_len = i_end-indexes[root]

    print(root, end=" ")
    # left
    order(i_start, i_start+left_len-1, p_start, p_start+left_len-1)
    # right
    order(i_end-right_len+1, i_end, p_end-right_len, p_end-1)

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

indexes = [0] * (n+1)

for i in range(n):
    indexes[inorder[i]] = i

order(0,n-1,0,n-1)
