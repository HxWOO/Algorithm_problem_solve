import sys
from collections import deque

sys.setrecursionlimit(30000)

T = int(sys.stdin.readline().rstrip())

def get_construct_time(i, dp, d, requirements):
    '''
    재귀적으로 top-down으로 건설시간을 구하는 함수
    '''
    if dp[i] != float('inf'):
        return dp[i]
    else:
        max = -1
        for req in requirements[i]:
            time = get_construct_time(req, dp, d, requirements)
            max = time if time > max else max
        dp[i] = max + d[i]
        return dp[i]

for _ in range(T):
    n, k = map(int, sys.stdin.readline().split())
    d = deque(map(int, sys.stdin.readline().split()))
    d.appendleft(0)
    requirements = [[] for _ in range(n+1)]
    dp = [float('inf')] * (n+1)

    for _ in range(k):  # O(K)
        x, y = map(int, sys.stdin.readline().split())
        requirements[y].append(x)

    w = int(sys.stdin.readline().rstrip())

    for i in range(1, n+1):  # O(n)
        if not requirements[i]:  # 선행 조건으로 필요한 건물이 없는 경우
            dp[i] = d[i]
    
    get_construct_time(w, dp, d, requirements)
    
    print(dp[w])
