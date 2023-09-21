import sys

s = [0, 0, 0]
while True:
    s.clear()
    s = list(map(int, sys.stdin.readline().split()))
    s.sort()
    if sum(s) == 0:
        exit()
    elif (s[0]**2 + s[1]**2) == s[2]**2:
        print("right")
    else:
        print("wrong")
