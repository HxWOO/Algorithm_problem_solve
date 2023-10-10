import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(3*(n+1))]
dp[2] = 1
dp[3] = 1

for i in range(2, n):
    if dp[i*3] > dp[i] + 1 or dp[i*3] == 0:
        dp[i*3] = dp[i] + 1
    if dp[i*2] > dp[i] + 1 or dp[i*2] == 0:
        dp[i*2] = dp[i] + 1
    if dp[i+1] > dp[i] + 1 or dp[i+1] == 0:
        dp[i+1] = dp[i] + 1

print(dp[n])

'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

시간 제한이 빡빡하다면 DP를 생각하자 
'''