import sys

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().split())
    graph[p].append((c,w))
    graph[c].append((p,w))

def dfs(start, graph, n):
    stack = [(start,0)]
    d = [0] * (n+1)
    visited = [False] * (n+1)

    while stack:
        node, w = stack.pop()
        
        if visited[node]:
            continue
        visited[node] =True

        for n_node, n_w in graph[node]:
            if  not visited[n_node]:
                d[n_node] = w + n_w 
                stack.append((n_node, w + n_w))
    return d

firt_search = dfs(1, graph, n)
mx_idx = firt_search.index(max(firt_search))

second_search = dfs(mx_idx, graph, n)
print(max(second_search))