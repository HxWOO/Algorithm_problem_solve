import sys

n = int(sys.stdin.readline().rstrip())
pos_list = []

for i in range(n):
    pos_list.append(list(map(int, sys.stdin.readline().split())))

answer = 0
for i in range(n):
    x1, y1 = pos_list[i]
    x2, y2 = pos_list[(i+1) % n]  # 마지막 점 -> 첫 점 연결
    answer += x1 * y2 - x2 * y1

print(f"{abs(round(answer/2, 1)):.1f}")