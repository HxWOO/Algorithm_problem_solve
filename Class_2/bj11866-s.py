import sys
from collections import deque
from typing import List, Any

n, k = map(int, sys.stdin.readline().split())
deq = deque()

res = []
for i in range(1, n+1):
    deq.append(i)

while len(deq) != 0:
    deq.rotate(-(k-1))
    res.append(deq.popleft())

str_list = ', '.join(map(str, res))
print(f'<{str_list}>')
