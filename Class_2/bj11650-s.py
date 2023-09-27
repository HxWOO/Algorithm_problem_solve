import sys

n = int(sys.stdin.readline())

dots = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

new_dots = sorted(dots)

for dot in new_dots:
    print(*dot)
