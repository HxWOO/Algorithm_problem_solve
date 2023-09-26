import sys

n = int(sys.stdin.readline())

res = []
for i in range(n):
    act = []
    inp = list(sys.stdin.readline().split())
    if inp[0] == 'push':
        act.append(inp[1])
    elif inp[0] == 'top':
        try:
            res.append(act[-1])
        except:
            res.append(-1)
    elif inp[0] == 'size':
        res.append(len(act))
    elif inp[0] == 'pop':
        try:
            res.append(act.pop())
        except:
            res.append(-1)
    elif inp[0] == 'empty':
        if len(act) == 0:
            res.append(1)
        else:
            res.append(0)

for i in res:
    print(i)
