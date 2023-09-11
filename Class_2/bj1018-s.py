n, m = map(int, input().split())
s = []

for i in range(0, n):
    a = input()
    s.append(a)
cnt_list = []

for first_i in range(n-7):
    for first_j in range(m-7):
        cnt = 0
        for i in range(first_i, first_i+8):
            for j in range(first_j, first_j+8):
                if (i+j) % 2 == (first_i+first_j) % 2 and s[i][j] != s[first_i][first_j]:
                    cnt += 1
                elif (i+j) % 2 != (first_i+first_j) % 2 and s[i][j] == s[first_i][first_j]:
                    cnt += 1
        if cnt > 32:
            cnt = 64-cnt

        cnt_list.append(cnt)

print(min(cnt_list))
