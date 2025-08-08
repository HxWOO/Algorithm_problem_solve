import sys
from itertools import combinations_with_replacement
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
nest_rm_nums_li = list(Counter(nums).keys())

com_li = list(combinations_with_replacement(nest_rm_nums_li, m))
prev = None

for com in com_li:
    if com == prev:
        continue
    prev = com
    print(*com)