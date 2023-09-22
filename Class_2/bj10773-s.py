import sys

k = int(sys.stdin.readline())
li = []
for i in range(k):
    num = int(sys.stdin.readline())

    if num == 0:
        li.pop()
    else:
        li.append(num)

print(sum(li))
