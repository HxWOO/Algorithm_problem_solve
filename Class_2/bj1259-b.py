while True:
    s = input()
    if int(s) == 0:
        break

    s_len = len(s)

    mid = s_len//2

    if s[0:mid] == s[-1:-mid-1:-1]:
        print("yes")
    else:
        print("no")
