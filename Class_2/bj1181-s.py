from functools import cmp_to_key


def cmp(a, b):
    if len(a) > len(b):
        return 1
    elif len(a) < len(b):
        return -1
    elif a < b:
        return -1
    else:
        return 1


n = int(input())

s = []
for i in range(n):
    a = input()
    s.append(a)

s.sort(key=cmp_to_key(cmp))  # 본인이 만든 비교 함수로 정렬 가능

new_s = []
for i in s:
    if i not in new_s:
        new_s.append(i)
        print(i)
