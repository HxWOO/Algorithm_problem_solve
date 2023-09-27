import sys

n = int(sys.stdin.readline())
dots = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for dot in sorted(dots, key=lambda x: (x[1], x[0])):
    print(*dot)
