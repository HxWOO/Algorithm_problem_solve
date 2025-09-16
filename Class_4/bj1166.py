import sys
import math

MAX = 1000000000

N, L, H, W = map(int, sys.stdin.readline().split())


left = 0.0
right = min(L,H,W)
answer = 0.0
for _ in range(1000):
    mid = (left + right) / 2
    cnt = (int(L // mid) * int(H // mid) * int(W // mid))

    if cnt >= N:
        left = mid
        answer = mid

    else:
        right = mid

print(f"{answer:.10f}")