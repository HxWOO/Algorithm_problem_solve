import sys
sys.setrecursionlimit(300000)

preorder = list(map(int, sys.stdin.read().split()))

def postorder(start, end):
    if start > end:
        return
    
    root = preorder[start]
    
    # 오른쪽 서브트리 시작점 찾기
    idx = start + 1
    while idx <= end and preorder[idx] < root:
        idx += 1
    
    # 왼쪽, 오른쪽 재귀
    postorder(start+1, idx-1)   # 왼쪽
    postorder(idx, end)         # 오른쪽
    print(root)

postorder(0, len(preorder)-1)