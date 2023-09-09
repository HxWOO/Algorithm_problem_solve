t = int(input())
result_list = []

for i in range(0, t):
    h, w, n = map(int, input().split())
    result = (n % h) * 100 + n//h + 1
    if n%h == 0:
        result = h * 100 + n//h
    result_list.append(result)

for result in result_list:
    print(result)
