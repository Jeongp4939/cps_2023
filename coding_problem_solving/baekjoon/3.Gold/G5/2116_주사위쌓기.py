# 주사위 쌓기 G5
# 서로 붙어 있는 두 개의 주사위에서 아래에 있는 주사위의 윗면에 적혀있는 숫자는
# 위에 있는 주사위의 아랫면에 적혀있는 숫자와 같아야 한다
# 주사위 구조
#   A
# B C D E
#   F
# 주사위 개수는 10,000개 이하
# A-F/ B-D / C-E(A-0,B-1,C-2,D-3,E-4,F-5)

def dice_max(top,btm):
    temp = [1, 2, 3, 4, 5, 6]
    temp.remove(top)
    temp.remove(btm)
    return max(temp)

N = int(input())
dice = [list(map(int,input().split())) for _ in range(N)]

dice_map = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}   # 각 인덱스의 반대 편 인덱스 딕셔너리 생성
max_sum = 0

for i in range(6):                 # 0번 주사위의 천장 인덱스 선택
    dice_top = dice[0][i]
    dice_btm = dice[0][dice_map[dice[0].index(dice_top)]]

    sum_d = dice_max(dice_top,dice_btm)

    for j in range(1,N):
        dice_btm = dice_top
        dice_top = dice[j][dice_map[dice[j].index(dice_top)]]

        sum_d+=dice_max(dice_top,dice_btm)

    if max_sum<sum_d:
        max_sum=sum_d
print(max_sum)