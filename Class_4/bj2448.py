import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline().rstrip())

def star(x):
    if x == 3:
        return ["  *  ",
                " * * ",
                "*****"]
    
    arr = star(x // 2)
    result = []
    
    # 위쪽 삼각형
    for line in arr:
        result.append(" " * (x // 2) + line + " " * (x // 2))
    # 아래쪽 두 삼각형
    for line in arr:
        result.append(line + " " + line)
    
    return result

print("\n".join(star(n)))