import sys

n, k = map(int, sys.stdin.readline().split())
w_v_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [0] * (k+1)

# dp[i] = dp[i-w] + dp[w]

# 모든 물건에 대해 비교
for w, v in w_v_list:
    for i in range(k, w-1, -1): # 물건의 무게까지만 확인
        dp[i] = max(dp[i] , dp[i-w] + v)

print(dp[k])
