import sys

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i-1] == str2[j-1]:  # 문자가 같으면
            dp[i][j] = dp[i-1][j-1] + 1
        else:  # 문자가 다르면, 이전 str1, str2의 직전 값중 최대값
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])