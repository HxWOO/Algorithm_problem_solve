import sys

S = list(sys.stdin.readline().rstrip())
stack = []

lasers = 0
answer = 0
for idx, elm in enumerate(S):
	if elm == '(':
		stack.append((idx, elm))
	else:
		top_idx, top_val = stack.pop()
		if (idx - top_idx) == 1:  # 레이저
			answer += len(stack)
		else:
			answer += 1

print(answer)