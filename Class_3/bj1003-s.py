import sys

t = int(sys.stdin.readline().rstrip())
dp = [[1, 0], [0, 1]]

for i in range(1, 41):
    next_li = [dp[i-1][0]+dp[i][0], dp[i-1][1]+dp[i][1]]
    dp.append(next_li)

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(*dp[n])
