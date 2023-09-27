import sys

n, k = map(int, sys.stdin.readline().split())
dp = [1]
s = int()
if n > n-k:
    s = n
else:
    s = n-k

for i in range(1, s+1):
    dp.append(dp[i-1]*i)

print(dp[n]//(dp[k]*dp[n-k]))
