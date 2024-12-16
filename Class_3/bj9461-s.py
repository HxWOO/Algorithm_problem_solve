import sys

t = int(sys.stdin.readline().rstrip())
dp = [0 for _ in range(101)]
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6, 101):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(dp[n])
