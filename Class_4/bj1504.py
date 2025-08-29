import sys
import heapq

N, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start, graph, trg):
    global N
    q = []
    q.append(start)
    path = [float('inf')] * (N+1)
    path[start[1]] = start[0]

    while q:
        w, v = heapq.heappop(q)

        if path[v] < w:
            continue

        for n_w, n_v in graph[v]:
            sum_w = w + n_w

            if path[n_v] > sum_w:
                path[n_v] = sum_w
                heapq.heappush(q, (sum_w, n_v))
    return path[trg]

v1_v2_dis = dijkstra((0,v1), graph, v2)
answer = min((dijkstra((0, 1), graph, v1) + v1_v2_dis + dijkstra((0,v2), graph, N)), 
                (dijkstra((0, 1), graph, v2) + v1_v2_dis + dijkstra((0,v1), graph, N)))

print(answer) if answer != float('inf') else print(-1)