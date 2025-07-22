import sys
import heapq as hq

n = int(sys.stdin.readline().rstrip())

heap = []
hq._heapify_max(heap)
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x:
        hq.heappush(heap, (-1) * x)
    elif not heap:
        print(0)
    else:
        print((-1) * hq.heappop(heap))