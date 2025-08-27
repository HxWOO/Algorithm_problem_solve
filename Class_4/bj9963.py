import sys

n = int(sys.stdin.readline().rstrip())

cols = set()   # 사용 중인 열
diag1 = set()  # 아래 대각선 (row+col)
diag2 = set()  # 위 대각선 (row-col)

def backtrack(row, N):
    if row == N:
        return 1

    count = 0
    for col in range(N):
        if col in cols or (row + col) in diag1 or (row - col) in diag2:  # 행, 열, 대각선 검사
            continue
        cols.add(col)
        diag1.add(row + col)
        diag2.add(row - col)

        count += backtrack(row + 1, N)

        # 백트랙 한번이 성공적으로 끝났으니깐 상태 복원
        cols.remove(col)
        diag1.remove(row + col)
        diag2.remove(row - col)
    return count

print(backtrack(0, N=n))