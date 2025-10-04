import sys

N, M = map(int, sys.stdin.readline().split())
answer = 0

min_s = float('inf')
min_p = float('inf')
for i in range(M):
    p, s = map(int, sys.stdin.readline().split())
    min_s = min(min_s, s)
    min_p = min(min_p, p)

# 아래 3가지 경우중에 가장 저렴한 경우가 있음
print(min(min_s * N, min_p*(N//6 + 1), min_p*(N//6) + min_s*(N%6)))
