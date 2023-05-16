# 행렬곱
def matmul(mat1,mat2):
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for z in range(N):
                res[i][j] += mat1[i][z]*mat2[z][j]%1000
    return res

# 분할정복
def power(a,b):
    if b==1:    # b==1 까지
        return a
    else:
        tmp = power(a,b//2) # a^(b//2)
        if b%2:
            return matmul(matmul(tmp,tmp),a)
        else:
            return matmul(tmp,tmp)

N,B = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
res = power(mat,B)

for row in res:
    print(*[i%1000 for i in row])
