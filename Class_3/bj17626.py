import sys
from collections import deque
import math

n = int(sys.stdin.readline().rstrip())

# dp 배열을 방문 여부 및 최소 개수 저장용으로 사용
# 초깃값은 무한대(inf)와 비슷한 큰 값으로 설정
dp = [float('inf')] * (n + 1)
dp[0] = 0

queue = deque([(0, 0)])  # (현재 숫자, 제곱수 개수)

while queue:
    current_num, count = queue.popleft()

    # 목표 숫자에 도달하면 종료
    if current_num == n:
        print(count)
        sys.exit()

    # 현재 개수가 이미 알려진 최소 개수보다 크면 더 탐색할 필요 없음
    if count >= dp[n]:
        continue

    # 제곱수들을 더해가며 다음 상태 탐색
    # n - current_num 까지만 확인하면 됨
    for i in range(int(math.sqrt(n - current_num)), 0, -1):
        next_num = current_num + i*i
        
        if next_num > n:
            continue

        # 더 적은 개수로 도달할 수 있는 경우에만 큐에 추가하고 dp 업데이트
        if dp[next_num] > count + 1:
            dp[next_num] = count + 1
            queue.append((next_num, count + 1))