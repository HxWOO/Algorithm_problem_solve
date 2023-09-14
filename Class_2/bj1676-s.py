n = int(input())

fact = [1]  # fibo[0] == 1
for i in range(1, n+1):
    fact.append(i*fact[i-1])

first_appear = []
str_fact = str(fact[-1])
for i in range(1, 10):
    first_appear.append(str_fact.rfind(str(i)))


print(len(str_fact)-max(first_appear)-1)
