import math
import sys
from collections import deque

n = int(sys.stdin.readline())
if n == 0:
    print(0)
    exit()

numbers = deque([int(sys.stdin.readline()) for i in range(n)])
numbers = deque(sorted(numbers))


def half_up(x):
    if math.floor(x) % 2 == 0:
        if x - math.floor(x) >= 0.5:
            return math.ceil(x)
        else:
            return math.floor(x)
    else:
        return round(x)


minus_num = half_up(n * 0.15)
while minus_num != 0:
    numbers.pop()
    numbers.popleft()
    minus_num -= 1

print(half_up(sum(numbers)/len(numbers)))
