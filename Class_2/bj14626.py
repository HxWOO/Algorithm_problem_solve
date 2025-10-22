import sys

nums = list(sys.stdin.readline().rstrip())
n = 13

broken_num_w = 0
total_sum = 0
for i in range(n):
    if i%2 == 0:
        if not nums[i].isnumeric():
            broken_num_w = 1
            continue
        total_sum += int(nums[i])

    else:
        if not nums[i].isnumeric():
            broken_num_w = 3
            continue
        total_sum += 3 * int(nums[i])
    
target = 10 - (total_sum % 10)
answer = 0

for i in range(10):
    if target == (i*broken_num_w)%10:
        answer = i

print(answer)