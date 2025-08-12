import sys
import heapq

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline
INF = float('inf')

# 도시의 개수(n), 버스의 개수(m)
n = int(input())
m = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n + 1)]

# 모든 버스 정보를 입력받기
for _ in range(m):
    v1, v2, w = map(int, input().split())
    # v1번 노드에서 v2번 노드로 가는 비용이 w라는 의미
    graph[v1].append((v2, w))

# 출발 도시와 도착 도시
start, end = map(int, input().split())

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

def dijkstra(start_node):
    # 우선순위 큐(힙) 사용
    pr_que = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(pr_que, (0, start_node))
    distance[start_node] = 0

    while pr_que:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pr_que)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(pr_que, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 도착 도시까지의 최단 거리 출력
print(distance[end])
