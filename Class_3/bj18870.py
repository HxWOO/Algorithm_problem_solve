# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

# 첫째 줄에 N이 주어진다.
# 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.
# 1 ≤ N ≤ 1,000,000, -10^9 ≤ Xi ≤ 10^9

# 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

import sys
from collections import Counter

n = int(sys.stdin.readline())
x_list = list(map(int, sys.stdin.readline().split()))
x_uniques = sorted(list(Counter(x_list).keys()))
x_prime_list = list()

x_dict = dict()
idx = 0
for x in x_uniques:
    x_dict[x] = idx
    idx += 1

for x in x_list:
    x_prime_list.append(x_dict[x])

print(*x_prime_list)