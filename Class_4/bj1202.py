import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

w_v_list = []
for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    heapq.heappush(w_v_list, (w,v))

bag_w_list = []
for _ in range(K):
    bag_w_list.append(int(sys.stdin.readline().rstrip()))

bag_w_list.sort()

answer = 0
candidate_jew = []
for cap in bag_w_list:
    # 담을 수 있는 보석을 모두 후보에 추가해놓음
    while w_v_list and w_v_list[0][0] <= cap:
        w, v = heapq.heappop(w_v_list)
        heapq.heappush(candidate_jew, -1*v)
    
    # 후보 중 젤 비싼걸 가져감
    if candidate_jew:
        answer += (-1*heapq.heappop(candidate_jew))

print(answer)
