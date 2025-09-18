import sys

N, M = map(int, sys.stdin.readline().split())

field = [[0] * N for _ in range(N)]

# 씨 뿌리기
for _ in range(M):
    x, y, l, f = map(int, sys.stdin.readline().split())
    for i in range(x, x + l):
        row = field[i]
        for j in range(y, y + l):
            row[j] = f

# (0,0)부터 (a-1,b-1)까지의 0의 개수
prefix_zero = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        cur = 1 if field[i][j] == 0 else 0  # 현재 칸이 빈칸인지 판단
        left = prefix_zero[i+1][j]          # 왼쪽 누적
        up = prefix_zero[i][j+1]            # 위쪽 누적
        diag = prefix_zero[i][j]            # 대각선 중복
        prefix_zero[i+1][j+1] = left + up - diag + cur  # 왼 + 위 - 중복

# 영역 (x1,y1) ~ (x2,y2) inclusive 에 0이 몇 개인지 O(1)로 반환
def count_zero(x1, y1, x2, y2):
    return prefix_zero[x2 + 1][y2 + 1] - prefix_zero[x1][y2 + 1] - prefix_zero[x2 + 1][y1] + prefix_zero[x1][y1]


# 한 변 길이 l 정사각형이 조건을 만족하는지 검사
# 시간 복잡도: 최악 O((N-l+1)^2 * l^2)
def valid(l):
    # 모든 가능한 왼쪽 상단 좌표(i, j)에 대해 검사
    limit = N - l + 1
    for i in range(limit):
        for j in range(limit):
            x2, y2 = i + l - 1, j + l - 1

            # 0이 1개라도 있으면 불가능
            if count_zero(i, j, x2, y2) > 0:
                continue

            # 씨앗 종류 판정
            # 최대 2종류까지만 허용
            kinds = set()
            can_sell = True

            for x in range(i, i + l):
                row = field[x]
                for y in range(j, j + l):
                    kinds.add(row[y])
                    if len(kinds) > 2:
                        can_sell = False
                        break
                if not can_sell:
                    break
            # 조건 만족하면 True 반환 (이분 탐색에서 mid가 가능하다는 뜻)
            if can_sell:
                return True

    # 모든 위치에서 실패하면 False
    return False


lo, hi = 1, N
best = 0

while lo <= hi:
    mid = (lo + hi) // 2
    # mid 길이의 정사각형이 존재하면 길이를 더 늘려본다
    if valid(mid):
        best = mid
        lo = mid + 1
    else:
        hi = mid - 1

# 문제는 '넓이'를 출력하므로 best*best
print(best * best)
