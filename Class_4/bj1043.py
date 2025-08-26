import sys

n, m = map(int, sys.stdin.readline().split())
truth_li = list(map(int, sys.stdin.readline().split()))
party_li = [list(map(int, sys.stdin.readline().split()))[1:] for _ in range(m)]

truth_set = set(truth_li[1:])

everyone_in_truth = False

while not everyone_in_truth:  # 진실을 아는, 알게 될 사람을 모두 찾는다
    everyone_in_truth = True
    for i in range(m):
        party_set = set(party_li[i])
        if len(party_set) == len(party_set - truth_set):  # party에 진실을 아는 자가 없는 경우
            continue
        elif len(party_set - truth_set) == 0:  # 파티의 모두가 진실을 아는 경우
            continue
        else: # 파티에 진실을 아는자와 모르는 자가 섞여 있는경우
            truth_set.update(party_set)
            everyone_in_truth = False
            # 만약 계속 union 해서 한번도 파티에 진실을 아는 자가 없는 경우를 안세게 된다면
            # everyone_in_truth = True로 종료

answer = 0

for party in party_li:  # 이제 완성된 진실 셋 을 가지고 비교
    party_set = set(party)
    if len(party_set) == len(party_set - truth_set):
        answer += 1

print(answer)