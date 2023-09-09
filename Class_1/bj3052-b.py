a = []

for i in range(0, 42):
    a.append(0)

for i in range(0, 10):
    i = int(input())
    a[i%42] += 1

print(42-a.count(0))
