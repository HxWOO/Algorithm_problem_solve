import sys
from collections import Counter

x = int(sys.stdin.readline().rstrip())

print(Counter(bin(x)).get('1'))