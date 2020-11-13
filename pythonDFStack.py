class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## constructing tree
root=TreeNode(4, 2, 7)
root.left=TreeNode(2, 1, 3)
# equal = root.left=TreeNode(2, 1, 3)

root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
root.right=TreeNode(7, 6, 9)
root.right.left=TreeNode(6)
root.right.right=TreeNode(9)
      #       4
      #   2       7
      # 1   3    6   9
# With recursion
## in order
def dfs(node: TreeNode):
    if not node:
        return
    dfs(node.left)
    values.append(node.val)
    dfs(node.right)

dfs(root)


# With stack
## inorder Shorter version
def inorder(self, root: TreeNode) -> List:
    result, stack = [], []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            result.append(node.val)
            root = node.right
    return result

# With stack
# longer version
inorder = []
node = root
stack = []
while True:
    # mylist.append(node)
    if node:
        stack.append(node)
        node = node.left
    elif stack:
        node = stack.pop()
        inorder.append(node.val)
        node = node.right
    else:
        break

print(inorder)

preorder = []
node = root
stack = []
while True:
    # mylist.append(node)
    if node:
        stack.append(node)
        preorder.append(node.val)
        node = node.left
    elif stack:
        node = stack.pop()
        node = node.right
    else:
        break
print(preorder)

# Construction of tree from a list
from collections import deque

data = [3,5,2,1,4,6,7,8,9,10,11,12,13,14]
n = iter(data)
tree = Node(next(n))
fringe = deque([tree])
while True:
    head = fringe.popleft()
    try:
        head.left = Node(next(n))
        fringe.append(head.left)
        head.right = Node(next(n))
        fringe.append(head.right)
    except StopIteration:
        break

# Constructing a right hand tree
#solution1
output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
from collections import deque

n = iter(output)
tree = TreeNode(next(n))
fringe = deque([tree])
while True:
    head = fringe.popleft()
    try:
        head.right = TreeNode(next(n))
        fringe.append(head.right)
    except StopIteration:
        break
return tree

#solution 2
head = TreeNode(output[0])
current = head
for i in output[1:]:
    current.right = TreeNode(i)
    current = current.right
return head
