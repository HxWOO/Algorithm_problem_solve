import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    dp[0][1], dp[1][1] = sticker[0][0], sticker[1][0]

    for i in range(2, n+1):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1] + sticker[0][i-1])
        dp[1][i] = max(dp[1][i-1], dp[0][i-1] + sticker[1][i-1])
    
    print(max(dp[0][-1], dp[1][-1]))
