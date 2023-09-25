import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
cnt = [0]*20000001

for num in n_list:
    cnt[num] += 1

res = []
for num in m_list:
    res.append(cnt[num])

print(*res)
