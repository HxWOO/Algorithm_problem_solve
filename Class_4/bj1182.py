import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

sum_dict = {}

for i in range(1, N):
    com_list = list(combinations(num_list, i))
    for li in com_list:
        total_num = sum(li)
        if not sum_dict.get(total_num):
            sum_dict[total_num] = 1
        else:
            sum_dict[total_num] += 1
    

offset = 0
if S == sum(num_list):
    offset += 1

if sum_dict.get(S):
    print(sum_dict.get(S) + offset)
else:
    print(offset)