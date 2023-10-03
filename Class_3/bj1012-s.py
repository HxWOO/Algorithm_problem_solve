import sys

sys.setrecursionlimit(5000)

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # down, up, right, left
t = int(sys.stdin.readline())

while t != 0:
    m, n, k = map(int, sys.stdin.readline().split())
    cabbage = [[0 for i in range(m)] for _ in range(n)]
    cnt = 0
    t -= 1


    def validation(c, d):
        global cabbage
        if 0 <= c < n and 0 <= d < m and cabbage[c][d] == 1:
            return True
        else:
            return False


    def dfs(a, b):
        global move
        global cabbage
        cabbage[a][b] = 0

        for i in range(4):
            new_a = a + move[i][0]
            new_b = b + move[i][1]
            if validation(new_a, new_b):
                dfs(new_a, new_b)


    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        cabbage[y][x] = 1

    for i in range(n):
        for j in range(m):
            if cabbage[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)
