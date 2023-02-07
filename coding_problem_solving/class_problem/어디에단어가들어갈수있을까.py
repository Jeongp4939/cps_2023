# import sys
# sys.stdin=open('input.txt','r')

def isOk(arr,k):
    ans_cnt = 0
    cnt_lst = []
    for i in range(len(arr)):
        cnt = 0
        cnt2 = 0
        for j in range(len(arr)):
            if j == 0 and arr[i][j] == 1:
                cnt=1
            elif arr[i][j-1] == arr[i][j] and arr[i][j] == 1:
                cnt+=1
                if j==(len(arr)-1):
                    cnt_lst.append(cnt)
            else:
                cnt_lst.append(cnt)
                cnt=1
        for j in range(len(arr)):
            if j == 0 and arr[j][i] == 1:
                cnt2=1
            elif arr[j-1][i] == arr[j][i] and arr[j][i]==1:
                cnt2+=1
                if j==(len(arr)-1):
                    cnt_lst.append(cnt2)
            else:
                cnt_lst.append(cnt2)
                cnt2=1
    for i in cnt_lst:
        if i==k:
            ans_cnt+=1
    return ans_cnt


for tc in range(1,int(input())+1):

    N,K = map(int,input().split())

    puzzle = [list(map(int,input().split())) for _ in range(N)]

    print(f'#{tc} {isOk(puzzle,K)}')