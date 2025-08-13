import sys
import itertools
import heapq

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
home_idx_list = []
chicken_idx_list = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home_idx_list.append((i,j))
        if board[i][j] == 2:
            chicken_idx_list.append((i,j))

# 1. 치킨 인덱스 리스트에서 m 만큼 고른, 인덱스 리스트를 만든다
chosen_idx_list = list(itertools.combinations(chicken_idx_list, m))

# 2. 각 인덱스에서의 도시 치킨 거리를 구한다
chicken_distance_list = []
for idx_li in chosen_idx_list:  # 각 후보 최적 치킨집 리스트
    chicken_distance = 0
    for home in home_idx_list:  # 각 집마다 치킨 거리 구하고
        h_x, h_y = home
        min_dis = float("inf")
        for i in range(m):
            val = 0
            val += abs(idx_li[i][0] - h_x)
            val += abs(idx_li[i][1] - h_y)
            if min_dis > val:
                min_dis = val
        chicken_distance += min_dis
    heapq.heappush(chicken_distance_list, chicken_distance) # 합한 값을 힙푸시

print(heapq.heappop(chicken_distance_list))