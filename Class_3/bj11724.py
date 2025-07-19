# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

gr = dict()
for i in range(1, n+1):
    gr[i] = []

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    gr[u].append(v)
    gr[v].append(u)

connected_nodes = [False for _ in range(n+1)]
connected_nodes[0] = True
ans = 0

for i in range(1, n+1):
    if connected_nodes[i]:  # 이미 다른 노드랑 연결 되었으면 다음 for문으로
        continue

    ans += 1  # 여기부턴 다른 노드랑 연결이 안되어 있단거니깐 ans++
    connected_nodes[i] = False
    queue = deque(gr[i])  # 큐에 i 노드랑 연결된 노드들 추가

    while queue:  # 큐가 빌때까지
        x = queue.pop()  # i랑 연결된 노드 x와 연결된 노드들도 찾기 
        if connected_nodes[x]:
            continue

        connected_nodes[x] = True
        for linked_node in gr[x]:  # 큐에 연결된 애들 또 추가
            queue.appendleft(linked_node)

print(ans)
