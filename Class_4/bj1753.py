import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline().rstrip()) - 1

graph = {}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if not graph.get(u-1):
        graph[u-1] = [(w, v-1)]
    else:
        graph[u-1].append((w, v-1))

def get_shortest_path(start_node):
    global graph
    global V
    q = []
    q.append((0, start_node))
    path = [float('inf') for _ in range(V)]
    path[start_node] = 0
    
    while q:
        w, cur_v = heapq.heappop(q)

        if not graph.get(cur_v):
            continue

        for n_w, next_node in graph[cur_v]:
            if path[next_node] > w + n_w:
                path[next_node] = w + n_w
                heapq.heappush(q, (w + n_w, next_node))
    
    return path

short_path = get_shortest_path(k)

for i in range(V):
    print(str(short_path[i]).upper())
