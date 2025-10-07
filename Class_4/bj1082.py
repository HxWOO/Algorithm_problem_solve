import sys
from collections import deque

# 입력 처리
N = int(sys.stdin.readline().rstrip())
prices = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())

# 숫자 가격-번호 매핑 (같은 가격 여러 개일 수 있음)
price_num_dic = {}
for i in range(N):
    price_num_dic.setdefault(prices[i], []).append(i)

# 가장 싼 가격
min_cost = min(prices)

# 아무것도 살 수 없는 경우
if M < min_cost:
    print(0)
    exit()

# 가능한 최대 자릿수
max_length = M // min_cost
if max_length == 0:
    print(0)
    exit()

# 가능한 길이 중 유효한 최대 길이 찾기
# (맨 앞자리가 0이 아닌 숫자로 만들 수 있는지)
valid_length = 0
for l in range(max_length, 0, -1):
    if l == 1:
        feasible = any(prices[d] <= M for d in range(N))
    else:
        feasible = any(prices[d] + (l - 1) * min_cost <= M for d in range(1, N))
    if feasible:
        valid_length = l
        break

if valid_length == 0:
    print(0)
    exit()

# 정답 수를 deque으로 저장
answer = deque()
remain = M

for i in range(valid_length):
    # 자리별 숫자 선택 (큰 숫자부터)
    for d in range(N - 1, -1, -1):
        # 첫 자리가 0이면 안 됨 (단, 길이 1인 경우 허용)
        if i == 0 and d == 0 and valid_length > 1:
            continue
        cost = prices[d]
        # 이 숫자를 선택했을 때 남은 자리들을 최소비용으로 채울 수 있는가?
        if remain - cost >= (valid_length - i - 1) * min_cost:
            answer.append(d)
            remain -= cost
            break

print(*answer, sep='')
