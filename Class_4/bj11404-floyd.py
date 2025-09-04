import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[float('inf') for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for i in range(n):
    graph[i][i] = 0

def floyd_warshall(n, graph):
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

shortest_paths = floyd_warshall(n, graph)

for path in shortest_paths:
    path = list(map(lambda x: 0 if x == float('inf') else x, path))
    print(*path)