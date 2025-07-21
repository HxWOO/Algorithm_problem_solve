# 지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.
# 문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

# 지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)
# 다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.

# 각 지점에서 목표지점까지의 거리를 출력한다.
# 원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
integer_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt_map = [[-1 for _ in range(m)] for _ in range(n)]
d_pos = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 상 좌 하 우

target_pos = []
for i in range(n):
    for j in range(m):
        if integer_map[i][j] == 2:
            cnt_map[i][j] = 0
            target_pos.append(i)
            target_pos.append(j)
        elif integer_map[i][j] == 0:
            cnt_map[i][j] = 0

queue = deque()
queue.appendleft(target_pos)

while queue:
    x, y = queue.pop()
    
    for dx, dy in d_pos:
        next_x = x + dx
        next_y = y + dy

        if (0 <= next_x < n) and (0 <= next_y < m) and cnt_map[next_x][next_y] == -1:
            queue.appendleft([next_x, next_y])
            cnt_map[next_x][next_y] = cnt_map[x][y] + 1

for cnt in cnt_map:
    print(*cnt)

