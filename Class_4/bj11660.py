import sys

n, m = map(int, sys.stdin.readline().split())

num_board = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

sum_li = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    sum_axis = 0
    for j in range(n):
        sum_axis += num_board[i][j]
        if i == 0:
            sum_li[i][j] = sum_axis
        else:
            sum_li[i][j] = sum_axis  + sum_li[i-1][j]


def print_target_sums(st_x, st_y, end_x, end_y):
    global sum_li
    global num_board

    if st_x > 0 and st_y > 0:
        print(sum_li[end_x][end_y] - sum_li[st_x-1][end_y] - sum_li[end_x][st_y-1] + sum_li[st_x-1][st_y-1])
    elif st_x > 0 and st_y == 0:
        print(sum_li[end_x][end_y] - sum_li[st_x-1][end_y])
    elif st_x == 0 and st_y > 0:
        print(sum_li[end_x][end_y] - sum_li[end_x][st_y-1])
    else:
        print(sum_li[end_x][end_y])
    

for _ in range(m):
    st_x, st_y, end_x, end_y = map(lambda x: int(x) - 1, sys.stdin.readline().split())  # 실제 인덱스에 맞게 -1
    print_target_sums(st_x, st_y, end_x, end_y)
