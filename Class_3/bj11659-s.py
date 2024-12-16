import sys

n, m = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    dp[i] = dp[i-1] + li[i-1]

for i in range(m):
    st, fin = map(int, sys.stdin.readline().split())

    print(dp[fin] - dp[st-1])
