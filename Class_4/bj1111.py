import sys

N = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().split()))

# 1. 각 숫자의 차를 구함
num_diff_list = list(map(lambda x, y: y - x, num_list[:-1], num_list[1:]))

def get_next_num():
    """
    다음 값을 구하는 함수
    다음 값이 여러개면 A, 없으면 B
    """
    global N
    global num_list
    global num_diff_list
    answer = 0

    # 2. len(num_diff_list) 가 1이나 0 밖에 없다면 규칙을 못 찾음 -> 암거나 넣어도 됨 A, 근데 0 하나 들어 있으면 첫번째 숫자 그대로
    if len(num_diff_list) < 2:
        if num_diff_list:
            return 'A' if num_diff_list[0] != 0 else num_list[0]
        else:
            return 'A'
    
    # 3. (앞수)*a + b 구함
    # 3-1. a 구하기, 0으로 나누면 안되니까 예외처리
    a = (num_diff_list[1] // num_diff_list[0]) if num_diff_list[0] != 0 else 0

    # 3-2. b 구하기, a가 0인 경우 b 만으로 반복이 이어져야 하므로 list 끝까지 검증해봄
    b = num_list[1] - num_list[0] * a
    for i in range(2, N):
        cur_b = num_list[i] - num_list[i-1] * a
        if b != cur_b:
            return 'B'

    # 4. 공식에 따라 output 구하고, 정수가 아니라면 B 출력
    answer = num_list[-1] * a + b
    if answer.is_integer():
        return int(answer)
    else:
        return 'B'

print(get_next_num())