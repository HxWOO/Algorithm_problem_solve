import sys
import heapq as hq

n = int(sys.stdin.readline().rstrip())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())

    if num:
        hq.heappush(heap, (abs(num), -1)) if num < 0 else hq.heappush(heap, (num, 1))
    else:
        if not heap:
            print(0)
        else:
            ans, pos = hq.heappop(heap)
            print(ans * pos)
