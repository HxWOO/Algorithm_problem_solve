import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
d_pos = [(0,1),(1,0),(-1,0),(0,-1)]

zero_li, virus_li = [], []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            zero_li.append((i,j))
        elif board[i][j] == 2:
            virus_li.append((i,j))

def bfs(wall_set):
    q = deque(virus_li)
    visited = [[False]*M for _ in range(N)]
    for r,c in virus_li:
        visited[r][c] = True

    virus_cnt = 0
    while q:
        r, c = q.popleft()
        for dr, dc in d_pos:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and board[nr][nc] == 0 and (nr,nc) not in wall_set:
                    visited[nr][nc] = True
                    q.append((nr,nc))
                    virus_cnt += 1
                    # 가지치기: 이미 최적 안전영역보다 못하면 중단
                    if virus_cnt >= len(zero_li) - 3 - answer:
                        return virus_cnt
    return virus_cnt

answer = 0
for walls in combinations(zero_li, 3):
    wall_set = set(walls)
    virus_cnt = bfs(wall_set)
    safe_area = len(zero_li) - 3 - virus_cnt
    answer = max(answer, safe_area)

print(answer)