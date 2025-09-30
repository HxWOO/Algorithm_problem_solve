import sys

N, M = map(int, sys.stdin.readline().split())

lands = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 하 우 상 좌

def dfs(start :tuple, level, visited):
    """
    start 랑 같은 영역인 애들을 구함
    높이도 같음
    0, N-1 행 / 0, M-1 행 닿으면 물 못 채움
    """
    global N, M
    global lands

    stack = []
    stack.append(start)
    # 물이 빠져나가는지 확인하는 flag
    is_absorbed = False

    # 시작부터 가장자리일수 있으니깐 확인
    if start[0] == 0 or start[0] == N-1 or start[1] == 0 or start[1] == M-1:
        is_absorbed = True
    visited[start[0]][start[1]] = True
    area = []
    
    while stack:
        r, c = stack.pop()
        area.append((r, c))

        for dr, dc in moves:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and lands[nr][nc] == level:
                if nr == 0 or nr == N-1 or nc == 0 or nc == M-1:
                    is_absorbed = True
                stack.append((nr,nc))
                visited[nr][nc] = True

    return is_absorbed, area

answer = 0
for lv in range(1, 9): # 높이가 1일때부터 확인
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if lands[i][j] == lv and not visited[i][j]:
                is_absorbed, area = dfs((i,j), lv, visited)
                for r, c in area: # 일단 방문한 곳의 높이를 채워주고
                    lands[r][c] += 1
                if not is_absorbed:  # 만약 물을 채울 수 있는 영역이면 그만큼 답에 더함
                    answer += len(area)
    del visited  # 메모리 관리 차원에서 delete

print(answer)