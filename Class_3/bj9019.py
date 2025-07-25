import sys
from collections import deque

d_op = ['D', 'S', 'L', 'R']

def op_D(n:int):
    n *= 2
    if n > 9999:
        return n % 10000
    return n

def op_S(n:int):
    if n == 0:
        return 9999
    return n - 1

def op_L(n:int):
    n = n//1000 + (n%1000)*10
    return n

def op_R(n:int):
    n = n//10 + (n%10)*1000
    return n

def get_queue(org_num:int, tg_num:int):
    queue = deque()
    created_num = [False] * 10000
    parent = [-1] * 10000
    used_op = [''] * 10000
    queue.append(org_num)
    created_num[org_num] = True

    while queue:
        cur_num = queue.popleft()
        if cur_num == tg_num:
            break
        
        for i in range(4):
            if i == 0:
                next_num = op_D(cur_num)
            elif i == 1:
                next_num = op_S(cur_num)
            elif i == 2:
                next_num = op_L(cur_num)
            else:
                next_num = op_R(cur_num)

            if not created_num[next_num]:
                queue.append(next_num)
                created_num[next_num] = True
                parent[next_num] = cur_num
                used_op[next_num] = d_op[i]
    
    
    method = deque()
    while tg_num != org_num:
        method.appendleft(used_op[tg_num])
        tg_num = parent[tg_num]
    
    return method



t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    A, B = map(int, sys.stdin.readline().split())
    print(*get_queue(A,B), sep='')
