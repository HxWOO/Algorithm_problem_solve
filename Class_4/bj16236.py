import sys
from collections import deque
import heapq

N = int(sys.stdin.readline().rstrip())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
directions = [(-1,0), (0,-1), (0,1), (1,0)]  # 상, 좌, 우, 하 로 하면 자동으로 조건 맞출 수 있을듯. (안되네, (좌 하)랑 (하, 좌)가 겹침)

def bfs(start, shark_size):
    global N, sea, directions
    q = deque()
    q.append((start[0], start[1], 0))
    is_visited = [[False for _ in range(N)] for _ in range(N)]
    is_visited[start[0]][start[1]] = True
    result = []  # 시간, x, y

    while q:
        x, y, t = q.popleft()

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and shark_size>=sea[nx][ny] and not is_visited[nx][ny]:
                q.append((nx, ny, t+1))
                is_visited[nx][ny] = True
                if 0 < sea[nx][ny] < shark_size:
                    heapq.heappush(result, (t+1, nx, ny))
    if result:
        return heapq.heappop(result)
    else:
        return (None, None, None)


# 상어 위치 찾기
shark_pos = []
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark_pos=[i,j]

make_help = False
answer = 0
shark_size = 2
fed_ones = 0
# 상어가 도움 요청할 때까지
while not make_help:
    # 상어가 떠난 자리엔 0
    sea[shark_pos[0]][shark_pos[1]] = 0
    # 먹이 찾기
    spent_time, nx, ny = bfs(shark_pos, shark_size)

    if spent_time is not None:
        fed_ones += 1
        shark_pos[0] = nx
        shark_pos[1] = ny
        answer += spent_time
    else:
        make_help = True

    if fed_ones == shark_size:
        fed_ones = 0
        shark_size += 1
    
print(answer)