import sys

n, m = map(int, sys.stdin.readline().split())
tree_heights = list(map(int, sys.stdin.readline().split()))

start, end = 0, max(tree_heights)
result = 0

while start <= end:
    mid = (start + end) // 2
    total_wood = sum(map(lambda x:x-mid if x>mid else 0, tree_heights))
    
    if total_wood >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
