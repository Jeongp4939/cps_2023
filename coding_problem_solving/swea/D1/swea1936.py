# 1:1 가위바위보, 가위는 1, 바위는 2, 보는 3

a, b = map(int, input().split())
if a - b == 1 or (a == 1 and b == 3):
    print('A')
else:
    print('B')