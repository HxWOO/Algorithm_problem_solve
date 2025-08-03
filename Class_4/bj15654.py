import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
nums = map(int, sys.stdin.readline().split())

li = permutations(nums,m)

for l in sorted(list(li)):
    print(*l)
