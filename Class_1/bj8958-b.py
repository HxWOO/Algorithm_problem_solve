n = int(input())
result_list = []

for i in range(0, n):
    a = input()
    cnt = 1
    result = 0
    for let in a:
        if let == 'O':
            result += cnt
            cnt += 1
        else:
            cnt = 1
    result_list.append(result)

for result in result_list:
    print(result)
