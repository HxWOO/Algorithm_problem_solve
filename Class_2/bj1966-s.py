t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    pr = list(map(int, input().split()))
    cnt = 0  # 출력된 문자의 수
    while True:
        if max(pr) == pr[0]:
            pr.pop(0)
            cnt += 1
            if m == 0:
                print(cnt)
                break
            else:
                m -= 1
                if m < 0:
                    m += len(pr)

        else:
            pr.append(pr.pop(0))
            m -= 1
            if m < 0:
                m += len(pr)

