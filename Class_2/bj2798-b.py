n, m = map(int, input().split())

numbers = list(map(int, input().split()))

adds = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            adds.append(numbers[i] + numbers[j] + numbers[k])


def minus_m(a):
    return a-m


adds = list(map(minus_m, adds))
adds.sort()

while adds[-1] > 0:
    adds.pop()

print(m + adds[-1])
