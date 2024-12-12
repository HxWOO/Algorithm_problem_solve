import sys
import math

n = int(sys.stdin.readline())

p_list = list(map(int, sys.stdin.readline().split()))
p_list.sort()

result = 0
# for i in range(n): math 모듈을 이용하는 법
#     result += math.fsum(p_list)
#     p_list.pop()

for i in range(1, n+1):  # 그냥 구현
    result += i*p_list.pop()

print(int(result))
