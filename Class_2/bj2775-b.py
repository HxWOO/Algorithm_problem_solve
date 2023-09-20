import sys

dp = [[i for i in range(15)] for j in range(15)]

t = int(sys.stdin.readline())

for i in range(1, 15):
    for j in range(1, 15):
        res = 0
        for k in range(1, j+1):
            res += dp[i-1][k]
        dp[i][j] = res

while t != 0:
    t -= 1
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(dp[k][n])
