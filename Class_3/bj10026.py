import sys
from collections import deque
import re

n = int(sys.stdin.readline().rstrip())
color_map = [sys.stdin.readline().rstrip() for _ in range(n)]  #  색깔 맵
d_pos = [(1,0), (-1,0), (0,-1), (0,1) ] # 하 상 좌 우


def get_area_cnt(color_map, n):
# 구역의 수
    cnt = 0
    que = deque()
    visited_node = [[False for _ in range(n)] for _ in range(n)]  # 방문한 노드 표시

    for i in range(n):
        for j in range(n):
            if visited_node[i][j]:
                continue
            else:
                visited_node[i][j] = True  # 이제 쓸거니깐 방문 표시  
        
            color = color_map[i][j]
            que.append((i,j))
        
            while que:
                x, y = que.pop()
                for d_x, d_y in d_pos:
                    next_x = x + d_x
                    next_y = y + d_y
                    # index 범위 안이고, 방문한적 없고, 색이 같다면 조건 통과
                    if 0 <= next_x < n and 0 <= next_y < n and not visited_node[next_x][next_y] and color_map[next_x][next_y] == color:
                        que.appendleft((next_x, next_y))
                        visited_node[next_x][next_y] = True
            cnt += 1 # 구역 하나 돌았으니깐 구역수 +1
    return cnt

ans1 = get_area_cnt(color_map, n)

# 적색 -> 녹색 변환
color_map_II = []
for color in color_map:
    color_map_II.append(re.sub('R','G', color))

ans2 = get_area_cnt(color_map_II, n)

print(ans1, ans2)
