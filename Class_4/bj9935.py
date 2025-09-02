import sys

org_string = list(sys.stdin.readline().rstrip())
bomb = list(sys.stdin.readline().rstrip())
LEN_BOMB = len(bomb)
stack = []

for let in org_string:
    stack.append(let)
    if stack[-1*LEN_BOMB:] == bomb:
        for _ in range(LEN_BOMB):
            stack.pop()

if stack:
    print(*stack, sep='')
else:
    print("FRULA")