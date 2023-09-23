import sys

n = int(sys.stdin.readline())

li = [sys.stdin.readline().split() for _ in range(n)]

for i in range(n):
    li[i][0] = int(li[i][0])
    li[i].insert(1, i)

li.sort()

for i in li:
    print(i[0], i[2])
