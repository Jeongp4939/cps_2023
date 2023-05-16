DIV = 1000000007
mat = [[1,1],[1,0]]

# 행렬곱
def matmul(mat1,mat2):
    res = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for z in range(2):
                res[i][j] += mat1[i][z]*mat2[z][j] % DIV
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

n = int(input())
res = power(mat,n)
print(res[0][1]%DIV)


