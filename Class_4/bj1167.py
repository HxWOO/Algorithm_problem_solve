import sys

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]


def dfs(start):
    """
    제일 멀리 있는 노드와 그 번호를 리턴하는 함수
    """
    stack = [(start, 0)]
    is_visited = [False for _ in range(n+1)]
    is_visited[start] = True

    far_node = start
    max_dist = 0

    while stack:
        cv, d = stack.pop()

        if d > max_dist:
            max_dist = d
            far_node = cv

        for nv, nd in graph[cv]:
            if not is_visited[nv]:
                is_visited[nv] = True
                stack.append((nv, d + nd))
    return max_dist, far_node


for i in range(1, n+1):
    inputs = list(map(int, sys.stdin.readline().split()))
    node = inputs[0]
    j = 1
    while inputs[j] != -1:
        graph[node].append((inputs[j], inputs[j+1]))
        j += 2

_, far = dfs(1)
answer, _ = dfs(far)

print(answer)