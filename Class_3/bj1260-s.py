import sys

n, m, v = map(int, sys.stdin.readline().split())  # 정점 수, 간선 수, 정점 번호

graph = [[] for _ in range(n)]  # 그래프 선언

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)  # 탐색하기 쉽게 -1 해서 넣어줌, 양방향으로 넣어줌

for i in range(n):
    graph[i].sort()  # 작은수부터 탐색할 수 있게 정렬

start = v - 1  # 시작 정점 번호
dfs_list = []


def dfs(start_v):
    global graph
    global dfs_list

    dfs_list.append(start_v)
    for k in range(len(graph[start_v])):
        if graph[start_v][k] not in dfs_list:
            next_v = graph[start_v][k]
            dfs(next_v)


idx = 0
bfs_list = [start]
while idx < len(bfs_list):
    now = bfs_list[idx]
    for k in range(len(graph[now])):
        if graph[now][k] not in bfs_list:
            bfs_list.append(graph[now][k])
    idx += 1

dfs(start)
dfs_list = list(map(lambda x: x + 1, dfs_list))
bfs_list = list(map(lambda x: x + 1, bfs_list))

print(*dfs_list)
print(*bfs_list)
