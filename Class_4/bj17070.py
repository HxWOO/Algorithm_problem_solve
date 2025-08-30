import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]  # 가로 세로 대각 의 형태로 온 경우의 수
dp[0][1][0] = 1  # 가로로 놓여있으니깐

for i in range(2,n):  # 첫행 채워주기
    if house[0][i] == 1:
        break
    dp[0][i][0] = dp[0][i-1][0]

# dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]   가로로 오는 경우
# dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]    세로로 오는 경우
# dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]   대각선으로 오는 경우

for i in range(1, n):  # dp[i][j] = max(dp[i-1][j][1] + dp[i-1][j][2], dp[i][j-1][0] + dp[i][j-1][2], dp[i-1][j-1][2])
    for j in range(1, n):
        if house[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
            
            if house[i-1][j] == 0 and house[i][j-1] == 0:
                dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[n-1][n-1]))