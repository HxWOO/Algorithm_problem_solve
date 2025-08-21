import sys
import math

n = int(sys.stdin.readline().rstrip())
dp = [0] * (n+1)

dp[1] = 1  # 초기화
dp[2] = 2
# i 번째 사람과 악수 o/x
# i-1이 악수 안한 상태일때만 i가 악수할 수 있음 -> dp[i-2] 경우
# i가 악수 안한 경우는 무조건 올 수 있음 -> dp[i-1] 경우
# dp[i] = dp[i-1] + dp[i-2], 피보나치 수열

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10

print(dp[n])