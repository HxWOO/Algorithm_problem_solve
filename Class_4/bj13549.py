import sys
import heapq

n, k = map(int, sys.stdin.readline().split())

def get_min_walk():
    dp = [float('inf')] * 100001
    dp[n] = 0
    q = []
    q.append([dp[n], n])
    while dp[k] == float('inf') and q:
        sec, loc = heapq.heappop(q)

        for i in range(3):
            n_sec, n_loc = -1, -1

            if i == 0:  # 순간이동
                n_loc = loc*2
                n_sec = sec
            elif i == 1 :  # +1 로 걷기
                n_loc = loc +1
                n_sec = sec +1
            else:  # -1로 걷기
                n_loc = loc -1
                n_sec = sec +1
            
            if not (0 <= n_loc < 100001):  # index 범위 벗어남
                continue

            if dp[n_loc] != float('inf'):  # 이미 들른 곳이면 continue
                continue

            if dp[n_loc] > n_sec:
                dp[n_loc] = n_sec
                heapq.heappush(q, [n_sec, n_loc])

    return dp[k]

if n >= k:
    print(n-k)
else:
    print(get_min_walk())