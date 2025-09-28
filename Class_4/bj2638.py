import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 하 우 상 좌

def bfs(board, cheeses: set):
    """
    항상 0,0 에서 BFS를 시작해서 외부 공기 셋을 반환하는 함수
    """
    global N, M

    q = deque()
    q.append((0,0))
    visited = [[False for _ in range(M)] for _ in range(N)]

    while q:
        r, c = q.popleft()
        for dr, dc in moves:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and board[nr][nc] != 1:
                visited[nr][nc] = True
                q.append((nr,nc))
    return visited



cheeses = set()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            cheeses.add((i,j))

time = 0
while cheeses:
    time += 1
    # 0. 외부 공기 영역 구함
    is_atmosphere = bfs(board, cheeses)

    # 1. 각 치즈들에 대해 녹을 치즈인지 검사
    melting_cheeses = set()
    for r, c in cheeses:
        cnt = 0
        for dr, dc in moves:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and is_atmosphere[nr][nc]:
                cnt += 1
        if cnt > 1:
            melting_cheeses.add((r,c))
    
    # 2. 구해진 녹을 치즈 자리를 0으로 바꿈
    for r, c in melting_cheeses:
        board[r][c] = 0
    
    # 3. 녹을 치즈를 치즈 셋에서 없앰
    cheeses = cheeses.difference(melting_cheeses)

print(time)