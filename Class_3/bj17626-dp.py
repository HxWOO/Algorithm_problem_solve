import sys
import math

n = int(sys.stdin.readline().rstrip())
dp = [5] * (n+1)
num_li = []

for i in range(1, n+1):
    if math.sqrt(i).is_integer():
        dp[i] = 1
        num_li.append(i)
        continue
    for num in num_li:
        if dp[i] > dp[i-num] + 1:
            dp[i] = dp[i-num] + 1

print(dp[n])
