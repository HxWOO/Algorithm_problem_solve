a = range(0, 9)
b = []

for i in a:
    i = int(input())
    b.append(i)

print(max(b))
print(b.index(max(b))+1)
