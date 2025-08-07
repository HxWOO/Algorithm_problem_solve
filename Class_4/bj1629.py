import sys

a, b, c = map(int, sys.stdin.readline().split())

def power(a, b, c):
    # 베이스 케이스: b가 1이면 a % c를 반환
    if b == 1:
        return a % c
    
    # b를 반으로 나누어 재귀적으로 호출
    res = power(a, b // 2, c)
    
    # b가 짝수인 경우
    if b % 2 == 0:
        return (res * res) % c
    # b가 홀수인 경우
    else:
        return (res * res * a) % c

result = power(a, b, c)
print(result)
