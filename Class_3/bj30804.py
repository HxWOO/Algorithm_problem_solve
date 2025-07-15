# 첫 줄에 과일의 개수 N이 주어집니다. (1 <= N <= 200,000)
# 둘째 줄에 탕후루에 꽂힌 과일을 의미하는  N개의 정수 S_1, ... , S_N이 공백으로 구분되어 주어집니다

# 문제의 방법대로 만들 수 있는 과일을 두 종류 이하로 사용한 탕후루 중에서, 
# 과일의 개수가 가장 많은 탕후루의 과일 개수를 첫째 줄에 출력하세요.
import sys
from collections import Counter, deque

n = int(sys.stdin.readline().rstrip())
fruits = sys.stdin.readline().split()
answer = 1
left_end = 0
c = Counter(fruits[0:1])

for right_end in range(1, n):
    
    if fruits[right_end] in c:
        c[fruits[right_end]] += 1
    else:
        c[fruits[right_end]] = 1
        
        while len(c) > 2:
            c[fruits[left_end]] -= 1
            if c[fruits[left_end]] == 0:
                del c[fruits[left_end]]
            left_end += 1
    answer = max(answer, c.total())

print(answer)