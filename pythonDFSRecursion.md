


```python

def preorder(root):
  return [root.val] + preorder(root.left) + preorder(root.right) if root else []

def inorder(root):
  return  inorder(root.left) + [root.val] + inorder(root.right) if root else []

  def postorder(root):
    return  postorder(root.left) + postorder(root.right) + [root.val] if root else []

```
