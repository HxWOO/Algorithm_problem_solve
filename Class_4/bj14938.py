import sys

n, m, r = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))

graph = [[float('inf') for _ in range(n)] for _ in range(n)]

for i in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], l)
    graph[b-1][a-1] = min(graph[b-1][a-1], l)

for i in range(n):
    graph[i][i] = 0

def floyd_warshall(n, graph):
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

shortest_path = floyd_warshall(n, graph)
answer = 0
for path in shortest_path:
    itm_cnt = 0
    for i in range(n):
        if path[i] <= m:
            itm_cnt += t[i]
    answer = max(answer, itm_cnt)

print(answer)
        