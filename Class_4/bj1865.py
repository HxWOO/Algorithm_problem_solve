import sys

TC = int(sys.stdin.readline().rstrip())


def bellmanFord(graph_edges, n, start):
    dist = [float('inf')] * (n+1)
    dist[start] = 0

    # V-1 번 완화
    for _ in range(0, n):
        for u, v, w in graph_edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # 음수 사이클 확인
    # 만약 값이 변한다면 음수 사이클이 있다는 뜻        
    for u, v, w in graph_edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return dist, True
    
    return dist, False


for _ in range(TC):
    n, m, w = map(int, sys.stdin.readline().split())
    edge_list = []
    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        edge_list.append((s, e, t))
        edge_list.append((e, s, t))
    
    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        edge_list.append((s, e, -1*t))
    
    # 가상의 노드 추가
    for i in range(1, n+1):
        edge_list.append((0, i, 0))

    
    shortest_paths, has_cycle = bellmanFord(edge_list, n, 0)
    
    print("YES") if has_cycle else print("NO")

