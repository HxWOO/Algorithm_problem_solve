import sys

n = int(sys.stdin.readline())

counts = [0]*10001
for i in range(n):
    num = int(sys.stdin.readline())
    counts[num] += 1

for i in range(1, 10001):
    while counts[i] != 0:
        print(i)
        counts[i] -= 1
