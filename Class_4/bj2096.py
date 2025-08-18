import sys
import heapq
from collections import deque

n = int(sys.stdin.readline().rstrip())

max_li = [0, 0, 0]
min_li = [0, 0, 0]
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())

    # 최댓값, 최소값 저장
    prev_max0, prev_max1, prev_max2 = max_li
    prev_min0, prev_min1, prev_min2 = min_li

    max_li[0] = max(prev_max0, prev_max1) + a
    max_li[1] = max(prev_max0, prev_max1, prev_max2) + b
    max_li[2] = max(prev_max1, prev_max2) + c

    min_li[0] = min(prev_min0, prev_min1) + a
    min_li[1] = min(prev_min0, prev_min1, prev_min2) + b
    min_li[2] = min(prev_min1, prev_min2) + c

print(max(max_li), min(min_li))