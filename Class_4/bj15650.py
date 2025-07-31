from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())

li = list(combinations(range(1, n+1), m))

for num in li:
    print(*num)