import math
import sys

n, r, c = map(int, sys.stdin.readline().split())
res = 0
while n != 0:
    n -= 1
    size = 2 ** n

    if r < size and c < size:  # 1사분면
        pass
    elif r < size <= c:  # 2사분면
        res += size ** 2
        c -= size
    elif r >= size > c:  # 3사분면
        res += (size ** 2) * 2
        r -= size
    else:  # 4사분면
        res += (size ** 2) * 3
        r -= size
        c -= size

print(res)
