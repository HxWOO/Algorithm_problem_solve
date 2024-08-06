import sys

n, m = map(int, sys.stdin.readline().split())

heard = []
for i in range(n):
    heard.append(sys.stdin.readline().rstrip())

saw = []
for i in range(m):
    saw.append(sys.stdin.readline().rstrip())

set_heard = set(heard)
set_saw = set(saw)

heard_saw = set_heard & set_saw

total = sorted(list(heard_saw))
print(total.__len__())

for one in total:
    print(one)
