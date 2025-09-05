import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
	a, b, t = map(int, sys.stdin.readline().split())
	graph[a].append((t, b))

def dijkstra(start, graph):
	global N
	q = []
	q.append((0, start))
	path = [float('inf')] * (N+1)
	path[start] = 0
	
	while q:
		time, node = heapq.heappop(q)
		
		if path[node] < time:
			continue
		
		for n_t, n_node in graph[node]:
			n_time = time + n_t
			if n_time < path[n_node]:
				path[n_node] = n_time
				heapq.heappush(q, (n_time, n_node))
	return path

x_path = dijkstra(X, graph)
answer = 0
for i in range(1, N+1):
	if i == X:
		continue
	cur = dijkstra(i, graph)
	answer = max(answer, cur[X] + x_path[i])

print(answer)