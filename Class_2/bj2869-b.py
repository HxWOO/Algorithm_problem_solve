import math
import sys

a, b, v = map(int, sys.stdin.readline().split())

day = 0

print(math.ceil((v-b)/(a-b)))
