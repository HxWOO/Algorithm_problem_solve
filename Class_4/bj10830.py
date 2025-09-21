import sys

sys.setrecursionlimit(30000000)

n, b = map(int, sys.stdin.readline().split())
mat = [list(map(lambda x: int(x) % 1000, sys.stdin.readline().split())) for _ in range(n)]


def mul_mat(matrix1:list[list], matrix2:list[list], n):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000
    return result


def pow_mat(matrix:list[list], n, b):
    if b == 1:
        return matrix

    # 기본 거듭제곱 로직
    result = pow_mat(matrix, n, b // 2)
    result = mul_mat(result, result, n)

    # 만약 홀수면 곱하기 기본 행렬 추가
    if b % 2 == 1:
        result = mul_mat(result, matrix, n)
    
    return result


new_mat = pow_mat(mat, n, b)
for row in new_mat:
    print(*row)
