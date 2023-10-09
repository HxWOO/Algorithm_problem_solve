import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n)]
bacon = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


def bfs(x):
    global graph
    global bacon
    visited = [x]
    depths = [0 for _ in range(n)]

    start = [0, 1]
    queue = deque()
    queue.append(x)

    while len(visited) < n:
        top = queue.popleft()
        for fr in graph[top]:
            start[0] = fr
            start[1] = depths[top] + 1
            if fr not in visited:
                visited.append(fr)
                queue.append(fr)
                depths[fr] = start[1]

    return depths


for i in range(n):
    li = bfs(i)
    bacon.append(sum(li))

print(bacon.index(min(bacon)) + 1)
