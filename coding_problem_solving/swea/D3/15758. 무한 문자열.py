for t in range(1, int(input())+1):
    S, T = input().split()
    if S*len(T) == T*len(S):
        print(f'#{t} yes')
    else:
        print(f'#{t} no')