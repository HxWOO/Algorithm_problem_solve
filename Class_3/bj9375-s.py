import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    cloths = dict()
    result = 1

    for k in range(n):
        cl = sys.stdin.readline().split()
        if cloths.get(cl[1]) is not None:
            cloths[cl[1]] += 1
        else:
            cloths[cl[1]] = 1

    for num in cloths.values():
        result *= num+1

    print(result-1)
