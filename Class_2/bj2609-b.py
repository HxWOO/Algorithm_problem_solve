n, m = map(int, input().split())
if n > m:
    a, b = n, m
else:
    a, b = m, n

r = 1
while r != 0:
    r = a % b
    a = b
    b = r


print(a)
print(n*m//a)
