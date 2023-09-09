n = int(input())

c = []

for i in range(0, n):
    a = input()
    num = int(a.__getitem__(0))
    b = ''
    for let in a[2:]:
        b += let*num
    c.append(b.split())

for result in c:
    print(str(result.__getitem__(0)))
