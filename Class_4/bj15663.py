import sys
from itertools import permutations
from collections import Counter

n, m = map(int, (sys.stdin.readline().split()))
num_li = list(map(int, sys.stdin.readline().split()))
num_cnt = Counter(num_li)

com_li = sorted(list(permutations(num_li, m)))

prev_com = (-1, -1)
for com in com_li:
    if prev_com == com:
        continue
    else:
        print(*com)
    prev_com = com

