import sys

N = int(sys.stdin.readline().rstrip())
target = int(sys.stdin.readline().rstrip())


def is_target(num):
    global target

    if num == target:
        return True
    else:
        return False


def snail():
    global N
    result = [[0 for _ in range(N)] for _ in range(N)]
    start = 0
    end = N-1
    num = N ** 2
    dir = 0
    pos = (0,0)

    while num > 0:
        dir %= 4
        if dir == 0:  # 아래로
            for r in range(start, end+1):
                result[r][start] = num
                if is_target(num):
                    pos = (r+1, start+1)
                num -= 1
                
        elif dir == 1:  # 오른쪽
            for c in range(start+1, end+1):
                result[end][c] = num
                if is_target(num):
                    pos = (end+1, c+1)
                num -= 1
        elif dir == 2:  # 위로
            for r in range(end-1, start-1, -1):
                result[r][end] = num
                if is_target(num):
                    pos = (r+1, end+1)
                num -= 1
        elif dir == 3:  # 좌로
            for c in range(end-1, start, -1):
                result[start][c] = num
                if is_target(num):
                    pos = (start+1, c+1)
                num -= 1
            # 끝났으니까 start, end 값 조정
            start += 1
            end -= 1

        dir += 1
    
    return pos, result


answer_pos, answer_list = snail()
for ans in answer_list:
    print(*ans)
print(*answer_pos)