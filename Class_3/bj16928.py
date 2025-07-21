import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

# 사다리와 뱀 정보를 저장할 딕셔너리
ladder_snake_map = dict()
for _ in range(n + m):
    x, y = map(int, sys.stdin.readline().split())
    # 1-100 범위를 0-99 인덱스로 변환
    ladder_snake_map[x - 1] = y - 1

# 각 칸에 도달하기 위한 최소 주사위 횟수를 저장 (-1은 아직 방문하지 않음을 의미)
board = [-1] * 100

# BFS를 위한 큐
queue = deque()

# 시작점(1번 칸 -> 0번 인덱스) 설정
board[0] = 0
queue.append(0)

while queue:
    # 큐의 맨 앞에서 원소를 꺼냄
    current_pos = queue.popleft()

    # 100번 칸(99번 인덱스)에 도달했다면 종료
    if current_pos == 99:
        print(board[current_pos])
        break

    # 주사위 굴리기 (1~6)
    for dice_roll in range(1, 7):
        next_pos = current_pos + dice_roll

        # 보드 범위를 벗어나지 않는지 확인
        if next_pos < 100:
            # 사다리나 뱀을 타야 하는 경우
            if next_pos in ladder_snake_map:
                next_pos = ladder_snake_map[next_pos]
            
            # 아직 방문하지 않은 칸이라면
            if board[next_pos] == -1:
                # 현재 칸까지의 횟수 + 1 로 다음 칸의 횟수 기록
                board[next_pos] = board[current_pos] + 1
                queue.append(next_pos)
