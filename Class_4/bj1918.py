import sys
from collections import deque

s = list(sys.stdin.readline().rstrip())

def shunting_yard(s:list['str']):

    precedence = {'(':0, '+':1, '-':1, '*':2, '/':2}

    output = deque()
    op_stack = []

    for token in s:
        if token.isalpha():  # 피연산자 일때
            output.append(token)
        
        elif token == '(':  # 왼쪽 괄호는 그냥 넣기
            op_stack.append(token)
        
        elif token == ')':  # 오른쪽 괄호일때, 왼쪽 괄호 나올때까지의 연산자 전부 다 꺼냄
            while op_stack and op_stack[-1] != '(':
                output.append(op_stack.pop())
            op_stack.pop()  # '(' 버리기
        else:  # 연산자일때
            while op_stack and op_stack[-1] != '(' and precedence[op_stack[-1]] >= precedence[token]:  # 스택의 탑 부분이 현재 연산자보다 우선순위 높은 연산자면 다 꺼냄
                output.append(op_stack.pop())
            op_stack.append(token)
        
    while op_stack:  # 스택에 남은 연산자들 꺼내줌
        output.append(op_stack.pop())
    
    return output

print(*shunting_yard(s), sep='')