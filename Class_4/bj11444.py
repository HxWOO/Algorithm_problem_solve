import sys

N = int(sys.stdin.readline().rstrip())
MOD_NUM = 1000000007

def matmul_2x2(a: list[list[int]], b: list[list[int]]):
    """
    2x2 행렬 끼리의 곱셈
    """
    global MOD_NUM
    return_mat = [[0,0], [0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                return_mat[i][j] += a[i][k] * b[k][j]
            return_mat[i][j] %= MOD_NUM
    
    return return_mat


def mat_pow(mat, n):
    """
    이진 거듭제곱으로 행렬 A^n 계산
    """
    result = [[1,0], [0,1]]
    base = mat
    while n > 0:
        if n & 1:  # 홀수면
            result = matmul_2x2(result, base)
        base = matmul_2x2(base, base)
        n >>= 1
    return result


def fib(n):
    global MOD_NUM
    if n ==0:
        return 0
    BASE = [[1, 1], [1, 0]]
    M = mat_pow(BASE, n-1)
    return M[0][0] % MOD_NUM


print(fib(N))