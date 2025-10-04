import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
S = list(map(int, sys.stdin.readline().split()))

# card_positions[i]는 i번 카드의 현재 위치를 저장
# 초기 상태: i번 카드는 i번 위치에 있음
card_positions = list(range(N))

# 초기 상태를 저장하여 사이클을 통한 불가능 판정
initial_card_positions = list(range(N))

count = 0
while True:
    # 현재 card_positions 상태가 목표를 만족하는지 확인
    # "i번 카드가 P[i]번 플레이어에게 가는가?"
    # i번 카드의 위치는 card_positions[i]이고, 이 위치의 카드는 card_positions[i] % 3 플레이어에게 간다.
    is_target = True
    for i in range(N):
        if card_positions[i] % 3 != P[i]:
            is_target = False
            break
    
    if is_target:
        print(count)
        sys.exit(0)

    # 셔플 횟수 증가 및 셔플 진행
    count += 1
    
    # 다음 카드 위치 계산
    next_card_positions = [0] * N
    for i in range(N):
        # i번 카드는 현재 card_positions[i] 위치에 있으므로,
        # 다음 위치는 S[card_positions[i]]가 된다.
        next_card_positions[i] = S[card_positions[i]]
    
    card_positions = next_card_positions

    # 초기 상태로 돌아왔다면, 목표 상태에 도달 불가능
    if card_positions == initial_card_positions:
        print(-1)
        sys.exit(0)
