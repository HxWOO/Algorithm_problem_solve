import sys

n = int(sys.stdin.readline())
S = set()
all_s = set()

for i in range(1, 21):
    all_s.add(i)

for i in range(n):
    way = sys.stdin.readline().split()
    if "add" in way:
        S.add(int(way[1]))
    elif "remove" in way:
        S.discard(int(way[1]))
    elif "check" in way:
        if int(way[1]) in S:
            print(1)
        else:
            print(0)
    elif "toggle" in way:
        if int(way[1]) in S:
            S.discard(int(way[1]))
        else:
            S.add(int(way[1]))
    elif "all" in way:
        S = set.copy(all_s)
    else:
        S.clear()

#clear
