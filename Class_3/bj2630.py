import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
color_paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt_col = [0,0]
is_made = [[False for _ in range(n)] for _ in range(n)]

def make_true(x, y, size):
    for i in range(x, x+size):
        for j in range(y, y+size):
            is_made[i][j] = True

def check_paper(x, y, size):
    color = color_paper[x][y]
    for i in range(x, x + size):
        for j in range (y, y + size):
            if color_paper[i][j] != color:
                return False
    cnt_col[color] += 1
    make_true(x, y, size)

length = n
while length > 0:
    for i in range(0, n, length):
        for j in range(0, n, length):
            if is_made[i][j]:
                continue
            if check_paper(i, j, length):
                continue
            

    length = length >> 1

print(cnt_col[0], cnt_col[1], sep='\n')