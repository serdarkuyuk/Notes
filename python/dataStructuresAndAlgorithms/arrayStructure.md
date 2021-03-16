# when to use

1. when to store multiple variable of same data type
2. random access

# when to avoid

1. same data type elements
2. reserve memory

```python
from array import *
arr = array('i', [1,2,2,4,45,])
# 'd' double 'f' float
#insert
arr1.insert(location, value)
```

creating array is constant time

# insert

at the end O(1)
at the begining O(n)

# traversal

arr.index(value)

# deletion

arr.remove(value)
O(n)

# Two dimentional arrays

adding row and column is O(mn)
