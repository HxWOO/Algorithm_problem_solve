import sys
import heapq

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]

for _ in range(m):
	a, b, c = map(int, sys.stdin.readline().split())
	graph[a].append((c, b))

def dijkstra(start, graph):
    q = []
    q.append((0, start))
    path = [float('inf')] * (n+1)
    path[start] = 0
    while q:
        cost, node = heapq.heappop(q)

        if path[node] < cost:
             continue
    
        for n_cost, n_node in graph[node]:
            sum_cost = cost + n_cost
            if sum_cost < path[n_node]:
                path[n_node] = sum_cost
                heapq.heappush(q, (sum_cost, n_node))

    return path[1:]

result = []
for i in range(1, n+1):
    result.append(dijkstra(i, graph))

for li in result:
    li = map(lambda x: 0 if x == float('inf') else x, li)
    print(*li)
	