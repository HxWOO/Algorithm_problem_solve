import sys
from collections import deque

s = list(sys.stdin.readline().rstrip())
# <ab cd>ef gh<ij kl>

deq = deque()
is_open = False
answer = ''
for i in range(len(s)):
    if s[i] == '<':
        is_open = True
        while deq:  # 열린 꺾쇠 전까지 위에서부터 print
            letter = deq.pop()
            answer += letter
    deq.append(s[i])
    if not is_open and s[i] == ' ':
        deq.pop()
        while deq:
            letter = deq.pop()
            answer += letter
        answer += ' '
    if s[i] == '>':
        is_open = False
        while deq:
            letter = deq.popleft()
            answer += letter

while deq:
    letter = deq.pop()
    answer += letter

print(answer)