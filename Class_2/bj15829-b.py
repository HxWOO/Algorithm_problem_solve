import sys

n = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()
has = list(map(lambda x: ord(x)-96, string))

res = 0
r = 31
M = 1234567891
for i in range(n):
    res += (r**i * has[i])

print(res%M)
