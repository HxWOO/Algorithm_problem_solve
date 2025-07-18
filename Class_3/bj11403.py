# 가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서,
# i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

# 첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다. 
# i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. 
# i번째 줄의 i번째 숫자는 항상 0이다.

# 총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다. 
# 정점 i에서 j로 가는 길이가 양수인 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.

# 1초, 256MB, 1 ≤ N ≤ 100
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
s = [list(map((lambda x: False if x=='0' else True), sys.stdin.readline().split())) for _ in range(n)]
queue = deque()

gr = dict()
for i in range(0, n):
    li = list()
    for k in range(n):
        if s[i][k]:
            li.append(k)
    gr[i] = li

ans = []
for i in range(n):
    queue = deque(gr[i])
    visited_li = [False for _ in range(n)]
    while queue:
        v = queue.pop()  # i가 방문하는 노드 v

        if not visited_li[v]:
            visited_li[v] = True
            for num in gr[v]:  # i가 방문한 v가 방문한 num 추가
                queue.appendleft(num)
                 
    ans.append(visited_li)

for li in ans:
    print(*map(int,li))
