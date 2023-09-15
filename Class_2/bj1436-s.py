n = int(input())

cnt = 0
num = 665
while cnt != n:
    num += 1
    if str(num).count("666") != 0:
        cnt += 1

print(num)
