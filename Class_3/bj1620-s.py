import sys

m, n = map(int, sys.stdin.readline().split())

int_key_dict = {}
str_key_dict = {}

for i in range(1, m+1):
    s = sys.stdin.readline().rstrip()
    int_key_dict[i] = s
    str_key_dict[s] = i

for i in range(n):
    s = sys.stdin.readline().rstrip()
    if s.isdecimal():
        print(int_key_dict.get(int(s)))
    else:
        print(str_key_dict.get(s))
