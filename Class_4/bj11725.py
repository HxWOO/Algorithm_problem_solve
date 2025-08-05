import sys
from collections import deque

# 재귀 깊이 제한 해제 (런타임 에러 방지)
sys.setrecursionlimit(10**6)

def bfs(graph, start_node, parent):
    queue = deque([start_node])
    parent[start_node] = start_node  # 루트 노드의 부모는 자기 자신으로 표시 (방문 처리)
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if parent[v] == 0:  # 아직 방문하지 않은 노드라면
                parent[v] = u   # 부모 노드를 기록
                queue.append(v)

n = int(sys.stdin.readline())

# 인접 리스트로 그래프 표현
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
# 각 노드의 부모를 저장할 리스트
parent = [0] * (n + 1)

# BFS를 이용해 각 노드의 부모 찾기
bfs(graph, 1, parent)

# 2번 노드부터 부모 출력
for i in range(2, n + 1):
    print(parent[i])
