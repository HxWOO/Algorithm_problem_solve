import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()
for i in range(n):
    order = list(sys.stdin.readline().split())

    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'pop':
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    else:
        try:
            print(queue[-1])
        except:
            print(-1)
