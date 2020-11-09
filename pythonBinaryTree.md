# Binary Tree
## class
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
## constructing tree
```python
root=TreeNode(4, 2, 7)
root.left=TreeNode(2, 1, 3)
equal = root.left=TreeNode(2, 1, 3)

root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
root.right=TreeNode(7, 6, 9)
root.right.left=TreeNode(6)
root.right.right=TreeNode(9)
# TreeNode{val: 4,
#     left: TreeNode{val: 2,
#         left: TreeNode{val: 1, left: None, right: None},
#         right: TreeNode{val: 3, left: None, right: None}},
#     right: TreeNode{val: 7,
#         left: TreeNode{val: 6, left: None, right: None},
#         right: TreeNode{val: 9, left: None, right: None}}}
# TreeNode{val: 4, left: TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}, right: TreeNode{val: 7, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 9, left: None, right: None}}}
```

# printing using qeue
```python
from collections import deque

def printTree(root):
    output = []
    stack = deque()
    stack.append(root)
    while stack:
        node = stack.popleft()
        if node:
            stack += node.left, node.right
            output.append(node.val)

    print(output)
```

## inverting binary tree
```python
stack = [root]
while stack:
    node = stack.pop()
    if node:
        node.left, node.right = node.right, node.left
        stack += node.left, node.right

printTree(root)
```
