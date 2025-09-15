import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

q = deque()
q.append(N)

dist = [-1] * 100001
cnt = [0] * 100001

dist[N] = 0
cnt[N] = 1

while q:
    x = q.popleft()

    for nx in (x*2, x+1, x-1):
        if 0 <= nx < 100001:
            if dist[nx] == -1:  # nx에 첫 방문
                dist[nx] = dist[x] + 1
                cnt[nx] = cnt[x]
                q.append(nx)
            
            # 같은 최단시간으로 방문
            elif dist[nx] == dist[x] + 1:
                cnt[nx] += cnt[x]

print(dist[K])
print(cnt[K])