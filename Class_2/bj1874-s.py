n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

nums = []
for i in range(n):
    nums.append(n-i)

stack = [0]
result = []
for num in arr:
    if stack[-1] < num:
        while stack[-1] < num:
            result.append("+")
            stack.append(nums.pop())
        stack.pop()
        result.append("-")

    elif num == stack[-1]:
        result.append("-")
        stack.pop()

    else:
        print("NO")
        exit()

for res in result:
    print(res)
