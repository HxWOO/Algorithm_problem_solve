k, n = map(int, input().split())
old_lan = []

for i in range(k):
    old_lan.append(int(input()))
res = 0


def binary(low, high):
    if high < low:
        return

    mid = (high+low) // 2
    n_count = 0
    global n
    global res

    for lan in old_lan:
        n_count += lan // mid
    if n_count >= n:
        res = mid
        binary(mid+1, high)
    else:
        binary(low, mid-1)


binary(0, max(old_lan)*2)
print(res)
