
sentence = input()

sentence.lower()

a = range(97, 123)
b = []  # [a, b, c, d, e ..., z]
for i in a:
    b.append(chr(i))

cnt_list = []

for let in b:
    cnt_list.append(sentence.lower().count(let))

t = 0
for cnt in cnt_list:
    if cnt == max(cnt_list):
        t += 1

if t > 1:
    print('?')
else:
    print(chr(cnt_list.index(max(cnt_list)) + 97).upper())
