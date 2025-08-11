import sys

class Node:
    def __init__(self, val: str):
        self.val = val
        self.left = None
        self.right = None

def preorder(node):
    if node is None:
        return ""
    return node.val + preorder(node.left) + preorder(node.right)

def inorder(node):
    if node is None:
        return ""
    return inorder(node.left) + node.val + inorder(node.right)

def postorder(node):
    if node is None:
        return ""
    return postorder(node.left) + postorder(node.right) + node.val


n = int(sys.stdin.readline().rstrip())
nodes = {chr(65 + i): Node(chr(65 + i)) for i in range(26)}  # A~Z 미리 생성

for _ in range(n):
    p, l, r = sys.stdin.readline().split()
    if l != '.':
        nodes[p].left = nodes[l]
    if r != '.':
        nodes[p].right = nodes[r]

root = nodes['A']  # 항상 A가 루트라고 가정

print(preorder(root))
print(inorder(root))
print(postorder(root))