import sys

n = int(input())
s = list(map(int, sys.stdin.readline().split()))
m = int(input())
v = list(map(int, sys.stdin.readline().split()))

sorted_list = sorted(s)

for i in range(m):
    cnt = 0
    high_idx = n-1
    low_idx = 0
    is_exist = False
    while high_idx >= low_idx:
        mid_idx = (high_idx+low_idx) // 2
        if sorted_list[mid_idx] < v[i]:
            low_idx = mid_idx+1
        elif sorted_list[mid_idx] > v[i]:
            high_idx = mid_idx-1
        else:
            print(1)
            is_exist = True
            break
    if not is_exist:
        print(0)
