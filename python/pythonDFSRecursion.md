
```Python
def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []
print(preorder(root))
```

```Python
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []
print(inorder(root))
```

```python

def postorder(root):
  return  postorder(root.left) + postorder(root.right) + [root.val] if root else []
print(postorder(root))

```
## Stack preorder
```python
def DFS(root):
    stack = []
    preorder = []
    while stack or root:
        if root:
            preorder.append(root.val)
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            root = root.right
    return preorder
print(DFS(root))
```


## Stack inorder
```python
def DFS(root):
    stack = []
    inorder = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            inorder.append(root.val)
            root = root.right
    return inorder
print(DFS(root))
```
