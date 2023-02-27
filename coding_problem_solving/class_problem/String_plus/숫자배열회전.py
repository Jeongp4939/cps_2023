def roll_matrix(arr, n):
    result = [[0 for row in range(n)] for col in range(n)]

    for i in range(n):
        for j in range(n):
            result[n - j - 1][i] = arr[i][j]

    return result

tc = int(input())

for testcase in range(tc):

    n = int(input())
    a = []

    for i in range(n):
        a.append(list(map(int, input().split())))

    roll_270 = roll_matrix(a, n)
    roll_180 = roll_matrix(roll_270, n)
    roll_90 = roll_matrix(roll_180, n)
    print(f'#{testcase+1}')
    for i in range(n):
        temp = ""
        for j in range(n):
            temp += str(roll_90[i][j])
        temp += ' '
        for j in range(n):
            temp += str(roll_180[i][j])
        temp += ' '
        for j in range(n):
            temp += str(roll_270[i][j])
        print(temp)
