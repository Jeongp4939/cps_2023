T = int(input())

def palindrome(s):
    len_s = 0
    for _ in s:
        len_s += 1
    for i in range(len_s//2+1):
        if s[i]!=s[-i-1]:
            return 0
    return 1

for tc in range(1,T+1):

    s = input().rstrip()

    print(f'#{tc} {palindrome(s)}')