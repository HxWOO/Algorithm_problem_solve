import math

m, n = map(int, input().split())

pn = [True]*(n+1)
pn[0] = False
pn[1] = False

for i in range(2, int(math.sqrt(n))+1):
    j = 2
    if pn[i]:
        while i*j <= n:
            pn[i*j] = False
            j += 1

for i in range(m, n+1):
    if pn[i]:
        print(i)
