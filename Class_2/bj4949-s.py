import sys
sentences = ['a']

while sentences[-1] != '.':
    sentences.append(sys.stdin.readline().rstrip())

sentences.pop(0)
sentences.pop()

for s in sentences:
    st = []

    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            st.append(s[i])
        elif s[i] == ')':
            try:
                if st[-1] == '(':
                    st.pop()
                else:
                    st.append('n')
                    break
            except:
                st.append('n')
                break
        elif s[i] == ']':
            try:
                if st[-1] == '[':
                    st.pop()
                else:
                    st.append('n')
                    break
            except:
                st.append('n')
                break

    if len(st) == 0:
        print("yes")
    else:
        print("no")
