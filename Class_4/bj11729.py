import sys
import heapq
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    v, w, c = map(int, sys.stdin.readline().split())
    graph[v].append((c, w))
    
def dijstra(start, end, board):
    global n

    q = []
    q.append((0, start, 0))

    shortest_d = [float('inf')] * (n+1)
    shortest_d[start] = 0
    prev_path = [float('inf')] * (n+1)
    prev_path[start] = 0

    while q:
        cost, v, prev_v = heapq.heappop(q)

        if cost > shortest_d[v]:
            continue
        if v == end:
            break

        for dc, nv in board[v]:
            nc = cost + dc

            if nc < shortest_d[nv]:
                shortest_d[nv] = nc
                prev_path[nv] = v
                heapq.heappush(q, (nc, nv, v))

    return prev_path, shortest_d

a, b = map(int, sys.stdin.readline().split())
shortest_path, s_d_li = dijstra(a, b, graph)

print(s_d_li[b])

answer_path = deque()
while b != a:
    answer_path.appendleft(b)
    b = shortest_path[b]
answer_path.appendleft(a)

print(len(answer_path))
print(*answer_path)