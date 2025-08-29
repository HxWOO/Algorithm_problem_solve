import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
move = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 상 좌 하 우
visited = [False] * 26

answer = 0
def dfs(r, c, depth):
    global answer
    answer = max(answer, depth)

    for dr, dc in move:
        next_r, next_c = r+dr, c+dc
        if 0<= next_r < R and 0<= next_c < C:
            alphabet = ord(board[next_r][next_c]) -65
            if not visited[alphabet]:
                visited[alphabet] = True
                dfs(next_r, next_c, depth + 1)
                visited[alphabet] = False # 다시 비교 가능하게 False로 바꿔줌

# 초기화
visited[ord(board[0][0])-65] = True
dfs(0, 0, 1)
print(answer)