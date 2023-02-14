# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스의 별로 인원수 N과 다음 줄에 N명이 고른 카드가 번호순으로 주어진다. 4≤N≤100
# 카드의 숫자는 각각 1은 가위, 2는 바위, 3은 보를 나타낸다.

# 1: 가위 2: 바위 3: 보
# 1,2 -> 2/ 2,3 -> 3, 1,3->1
# 비기면 앞사람이 승

def winner(a,b=0):
    if player_dic[a]>=player_dic[b]:
        if player_dic[a]==3 and player_dic[b]==1: return [b]
        else: return [a]
    else:
        if player_dic[a]==1 and player_dic[b]==3: return [a]
        else: return [b]


def tornament(players):
    n = len(players)
    if n<=2:
        return winner(*players)
    return tornament(players[:n//2])+tornament(players[n//2:]) if not n%2 else tornament(players[:n//2+1])+tornament(players[n//2+1:])

for tc in range(1,1+int(input())):
    n = int(input())
    player = list(map(int,input().split()))

    player_dic = {0:0}
    for i in range(n):
        player_dic[i+1] = player[i]
        player[i] = i+1

    while 1:
        if len(player)==1:
            break
        player = tornament(player)

    print(f'#{tc} {player[0]}')