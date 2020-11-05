#


![](http://www.globalnerdy.com/wp-content/uploads/2016/06/map-filter-reduce-in-emoji-1.png)

# map

```python
items = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, items))

squared = []
for i in items:
    squared.append(i**2)

#-----------------
Multiple functions

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

```


# Filter
```python
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
```

# Reduce
```Python
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
```
