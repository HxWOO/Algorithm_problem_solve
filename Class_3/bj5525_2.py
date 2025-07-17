import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

ans = 0
cnt = 0
idx = 1
while idx < M - 1:
    if S[idx-1] == 'I' and S[idx] == 'O' and S[idx+1] == 'I':
        cnt += 1
        if cnt == N:
            cnt -= 1  # 다음 i에서 또 패턴이 맞으면 바로 ans += 1 이 되도록   
            ans += 1
        idx += 1
    else:
        cnt = 0  # 패턴이 깨지면 바로 0부터 시작
    
    idx += 1

print(ans)