import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())

num = 1
q = deque()
q.append((b,1))
while num > 0 and q:
    num, cnt = q.popleft()
    if num%10 == 1:
        next_num = num//10
        if next_num == a:
            print(cnt+1)
            exit()
        n_cnt = cnt+1
        q.append((next_num,n_cnt))
    if num % 2 == 0:
        next_num = num//2
        if next_num == a:
            print(cnt+1)
            exit()
        n_cnt = cnt+1
        q.append((next_num,n_cnt))

print(-1)