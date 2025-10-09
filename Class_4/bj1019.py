import sys

N = int(sys.stdin.readline().rstrip())

answer = [0 for _ in range(10)]

start = 1
place = 1  # 자릿수 

def calc(x, place):
    global answer
    while x > 0:
        answer[x % 10] += place
        x //= 10


while start <= N:
    # --- 1단계: 끝 수(N)의 끝자리를 9로 맞추는 과정 ---
    while (N % 10) != 9 and start <= N:
        calc(N, place)
        N -= 1

    if start > N:
        break

    # --- 2단계: 시작 수(start)의 끝자리를 0으로 맞추는 과정 ---
    while (start % 10) != 0 and start <= N:
        calc(start, place)
        start += 1

    if start > N:
        break

    # --- 3단계: 0과 9로 정렬된 중간 블록을 한 번에 계산하는 과정 ---
    start //= 10
    N //= 10

    # 0부터 9까지의 숫자가 몇 번 나타나는지 계산합니다.
    num_of_blocks = N - start + 1
    for i in range(10):
        answer[i] += num_of_blocks*place

    # --- 4단계: 다음 자릿수로 이동 ---
    place *= 10

print(*answer, sep=' ')