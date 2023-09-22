import sys

t = int(sys.stdin.readline())

vps_list = [sys.stdin.readline().rstrip() for _ in range(t)]

for vps in vps_list:
    st = []

    for x in vps:
        if x == '(':
            st.append(x)
        else:
            try:
                st.pop()
            except:
                st.append('a')
                break
    if len(st) == 0:
        print("YES")
    else:
        print("NO")
