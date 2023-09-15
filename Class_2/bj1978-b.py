n = int(input())

pn = [True] * 1001

pn[0] = False
pn[1] = False

for i in range(2, 34):
    if pn[i]:
        j = 2
        while i*j <= 1000:
            pn[i*j] = False
            j += 1

cnt = 0
nums = list(map(int, input().split()))
for num in nums:
    if pn[num]:
        cnt += 1

print(cnt)
