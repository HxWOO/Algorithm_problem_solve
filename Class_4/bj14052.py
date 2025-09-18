import sys
import math

N, M = map(int, sys.stdin.readline().split())

board = [[map(int, sys.stdin.readline().split())] for _ in range(N)]

n_list = [0 for _ in range(M+1)]
s_list = [0 for _ in range(M+1)] 

for i in range(1, M+1):
    
    n_list[i] = n
    s_list[i] = s

for n, s in n_list, s_list:
    q = n


