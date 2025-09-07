import sys
from collections import deque

R, C, T = map(int, sys.stdin.readline().split())

room = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 하 우 상 좌

conditioner = []
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            conditioner.append((i,j))

def spread_air(room):
    global R, C
    global conditioner

    spread_map = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if room[i][j] != 0 and room[i][j] != -1:
                d_munji = room[i][j] // 5
                count = 0

                for dr, dc in moves:
                    nr, nc = (i + dr), (j + dc)
                    
                    # 방 범위 이내, 공기청정기가 아니어야 함
                    if (0 <= nr < R) and (0 <= nc < C) and room[nr][nc] != (-1):
                        spread_map[nr][nc] += d_munji
                        count += 1
                
                spread_map[i][j] -= d_munji * count
    
    for i in range(R):
        for j in range(C):
            room[i][j] += spread_map[i][j]


def clean_air(room):
    global R, C
    global conditioner

    for way, mpos in enumerate(conditioner):
        mr, mc = mpos
        cur_r, cur_c = mr, mc
        next_val = 0
        if way == 0:  # 청정기 상단부
            while cur_c < C-1: # 1. 청정기부터 오른쪽 끝까지
                cur_c += 1
                tmp = room[cur_r][cur_c]
                room[cur_r][cur_c] = next_val
                next_val = tmp

            while cur_r > 0:  # 2. 방의 첫 행까지
                cur_r -= 1
                tmp = room[cur_r][cur_c]
                room[cur_r][cur_c] = next_val
                next_val = tmp

            while cur_c > 0:  # 3. 방의 첫열까지
                cur_c -= 1
                tmp = room[cur_r][cur_c]
                room[cur_r][cur_c] = next_val
                next_val = tmp

            while cur_r < mr-1:  # 4. 공기 청정기 있는 열까지
                cur_r += 1
                tmp = room[cur_r][cur_c]
                room[cur_r][cur_c] = next_val
                next_val = tmp

            while cur_c < mc-1:  # 5. 공기 청정기 있는 곳까지
                cur_c += 1
                tmp = room[cur_r][cur_c]
                room[cur_r][cur_c] = next_val
                next_val = tmp

        else:  # 청정기 하단부
            while cur_c < C-1: # 1. 청정기부터 오른쪽 끝까지
                cur_c += 1
                tmp = room[cur_r][cur_c]
                room[cur_r][cur_c] = next_val
                next_val = tmp

            while cur_r < R-1:  # 2. 방의 마지막 행까지
                cur_r += 1
                tmp = room[cur_r][cur_c]
                room[cur_r][cur_c] = next_val
                next_val = tmp

            while cur_c > 0:  # 3. 방의 첫열까지
                cur_c -= 1
                tmp = room[cur_r][cur_c]
                room[cur_r][cur_c] = next_val
                next_val = tmp

            while cur_r > mr+1:  # 4. 공기 청정기 있는 행까지
                cur_r -= 1
                tmp = room[cur_r][cur_c]
                room[cur_r][cur_c] = next_val
                next_val = tmp

            while cur_c < mc-1:  # 5. 공기 청정기 있는 곳까지
                cur_c += 1
                tmp = room[cur_r][cur_c]
                room[cur_r][cur_c] = next_val
                next_val = tmp

for _ in range(T):
    spread_air(room)
    clean_air(room)

answer = 0
for row in room:
    answer += sum(row)

print(answer + 2)