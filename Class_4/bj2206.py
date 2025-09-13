import sys
from collections import deque
import heapq

N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우 하 좌 상

def get_path(board):
    global N, M
    global moves

    q = []
    start = (0, 0)
    q.append((0, start, False))
    path = [[[float('inf') for _ in range(2)] for _ in range(M)] for _ in range(N)]
    path[0][0][0] = 0  # 3번 차원은 벽을 깼으면 1, 안 깼으면 0
    path[0][0][1] = 0

    while q:
        cost, pos, is_broke = heapq.heappop(q)
        r, c = pos

        # 이미 최단 경로 구한 곳은 넘어감
        if (path[r][c][0] < cost and is_broke == False) and (path[r][c][1] < cost and is_broke == True):
            continue

        for dr, dc in moves:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M:
                if is_broke:  # 만약 이미 벽을 깬적 있으면
                    if path[nr][nc][1] > cost + 1:  # 해당 좌표에 벽이 없어야 함
                        if board[nr][nc] == 0:
                            path[nr][nc][1] = cost + 1
                            heapq.heappush(q, (cost+1, (nr, nc), True))
                        else:
                            continue
                else:  # 벽을 한번도 깬적 없으면
                    if path[nr][nc][0] > cost + 1:
                        if board[nr][nc] == 0:
                            path[nr][nc][0] = cost + 1
                            heapq.heappush(q, (cost+1, (nr, nc), False))
                        else:  # 두 경우 둘다 갈 수 있음
                            if path[nr][nc][1] > cost + 1:
                                path[nr][nc][1] = cost + 1
                                heapq.heappush(q, (cost+1, (nr,nc), True))
    return path[N-1][M-1]

min_dis = min(get_path(board))

if min_dis == float('inf'):
    print(-1)
else:
    print(min_dis+1)