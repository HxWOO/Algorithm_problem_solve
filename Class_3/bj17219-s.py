import sys

n, m = map(int, sys.stdin.readline().split())

pwds = dict()

for i in range(n):
    var = sys.stdin.readline().split()
    pwds[var[0]] = var[1]

for i in range(m):
    site = sys.stdin.readline().rstrip()
    print(pwds[site])
