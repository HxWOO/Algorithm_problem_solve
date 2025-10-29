import sys

n = int(sys.stdin.readline().rstrip())
sizes = list(map(int, sys.stdin.readline().split())) 
t, p = map(int, sys.stdin.readline().split())

total_order = 0
for size in sizes:
    total_order += (size // t)+1
    if (size % t) == 0:
        total_order -= 1

print(total_order)
print(n//p, n%p)