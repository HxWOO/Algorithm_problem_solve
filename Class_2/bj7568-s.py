import sys

n = int(sys.stdin.readline())

dung = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

rank = []

for i in range(n):
    cnt = 0
    for j in range(n):
        if dung[i][0] < dung[j][0] and dung[i][1] < dung[j][1]:
           cnt += 1

    rank.append(cnt+1)

print(*rank)
