import sys

'''
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
'''

polynoms = list(sys.stdin.readline().rstrip().split('-'))

list_to_minus = list()

for polynom in polynoms:
    numbers = polynom.split('+')
    numbers = list(map(int, numbers))
    list_to_minus.append(sum(numbers))

result = sum(list_to_minus) - 2 * list_to_minus.__getitem__(0)
print(-result)
