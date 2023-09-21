import sys

n = int(sys.stdin.readline())

s = n
i, j = 0, 0

while s > 4:
    s -= 5
    i += 1
if s == 0:
    print(i)
    exit()
elif s == 1 and n > 5:
    j = 2
    i -= 1
    print(i+j)
elif s == 2 and n > 11:
    j = 4
    i -= 2
    print(i+j)
elif s == 3:
    j = 1
    print(i+j)
elif s == 4 and n > 8:
    j = 3
    i -= 1
    print(i+j)
else:
    print(-1)
