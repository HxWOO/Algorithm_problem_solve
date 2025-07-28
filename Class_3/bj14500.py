import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  # 하 상 좌 우

max_val = 0

# 4개 연결된 block 찾는 dfs
def dfs(r, c, depth, current_sum):
    global max_val
    # 4일때, max 값 찾기
    if depth == 4:
        max_val = max(max_val, current_sum)
        return

    # 블록 순회
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, depth + 1, current_sum + board[nr][nc])
            visited[nr][nc] = False # 다음에 다시 돌아야하니깐, 다시 False로 바꿔주기

# 'ㅗ' 자 테트로미노 찾는 함수
def check_t_shape(r, c):
    global max_val
    
    t_shapes = [
        [(0, 0), (0, 1), (0, 2), (1, 1)],  # 기본 T shape
        [(0, 1), (1, 0), (1, 1), (1, 2)],  #  T shape
        [(0, 0), (1, 0), (2, 0), (1, 1)],  # Rotated T shape
        [(0, 1), (1, 1), (2, 1), (1, 0)]   # Rotated T shape
    ]

    for shape in t_shapes:
        temp_sum = 0
        is_valid = True
        for dr, dc in shape:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < n and 0 <= nc < m):
                is_valid = False
                break
            temp_sum += board[nr][nc]
        
        if is_valid:
            max_val = max(max_val, temp_sum)

# 모든 노드 순회
for r in range(n):
    for c in range(m):
        # dfs 시작
        visited[r][c] = True
        dfs(r, c, 1, board[r][c])
        visited[r][c] = False
        
        # 'ㅗ'자 테트로미노에 대해서 따로 체크
        check_t_shape(r, c)

print(max_val)
