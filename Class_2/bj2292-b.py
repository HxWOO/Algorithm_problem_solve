n = int(input())

#  0 = 1, 1 = 6, 2 = 6 * 2, 3 = 6 * 3
dis = 0
res = 1
while n > res:
    dis += 1
    res += 6*dis

print(dis+1)
