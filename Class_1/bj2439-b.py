
n = int(input())

a = range(1, n+1)

for i in a:
    b = '*'
    b *= i
    print(b.rjust(n, ' '))
