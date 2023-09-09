
a = map(int, input().split())

b = 0
for num in a:
    b += num*num

print(b % 10)
