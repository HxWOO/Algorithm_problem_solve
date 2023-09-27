import sys

n = int(sys.stdin.readline())

act = []
for i in range(n):

    inp = list(sys.stdin.readline().split())

    if inp[0] == 'push':
        act.append(inp[1])
    elif inp[0] == 'top':
        if len(act) == 0:
            print(-1)
        else:
            print(act[-1])
    elif inp[0] == 'size':
        print(len(act))
    elif inp[0] == 'pop':
        if len(act) == 0:
            print(-1)
        else:
            print(act.pop())
    elif inp[0] == 'empty':
        if len(act) == 0:
            print(1)
        else:
            print(0)
