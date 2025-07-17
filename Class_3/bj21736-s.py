# 첫째 줄에 두 정수 0<=N<=600, 0<=M<=600 이 주어짐
# 둘째 줄부터 N개의 줄에 캠퍼스 정보
# O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐이 보장
# 출력: 첫째 줄에 도연이가 만날 수 있는 사람의 수를 출력한다. 단, 아무도 만나지 못한 경우 TT를 출력

# 접근: 600*600 = 360000 번 이면 BF로 해도 시간 널널할듯?
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
campus_envs = [list(sys.stdin.readline()) for _ in range(n)]
visited_path = [[False for _ in range(m)] for _ in range(n)]
d_pos = [(1,0), (-1,0), (0,1), (0,-1)]

start_pos = [0, 0]
ans = 0

for i in range(n):
    for j in range(m):
        if campus_envs[i][j] == 'I':
            start_pos[0], start_pos[1] = i, j
    
queue = deque()
queue.append(start_pos)
visited_path[start_pos[0]][start_pos[1]] = True

while queue:
    x, y = queue.popleft()

    for dx, dy in d_pos:
        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < n and 0 <= new_y < m and not visited_path[new_x][new_y] and campus_envs[new_x][new_y] != 'X':
            if campus_envs[new_x][new_y] == 'P':
                ans += 1
            queue.append([new_x, new_y])
            visited_path[new_x][new_y]=True

if not ans:
    print("TT")
else:
    print(ans)
