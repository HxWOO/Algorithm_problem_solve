from string import ascii_lowercase

s = input()

alphabet_list = list(ascii_lowercase)
result = ''

for alphabet in alphabet_list:
    result += str(s.find(alphabet))
    result += ' '

print(result)
