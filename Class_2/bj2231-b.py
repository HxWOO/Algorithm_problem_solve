res = []
n = input()

for i in range(1, int(n)+1):
    result = i
    for j in str(i):
        result += int(j)

    if result == int(n):
        res.append(i)

res.sort()
try:
    print(res[0])
except:
    print(0)
