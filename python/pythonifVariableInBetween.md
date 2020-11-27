#Checking if a coordinate is in some boundaries


Instead of if something is out
```python
def legalCoord(self, i, j):
    # lengthColumn, lengthRow
    if i < 0 or i >= self.lengthRow or j < 0 or j >= self.lengthColumn:
        return False
    else:
        return True
```
Try this
```python
return False if i < 0 or i >= self.lengthRow or j < 0 or j >= self.lengthColumn else True
```

Think about if something in the boudries
```python
def legalCoord(self, i, j):
    # lengthColumn, lengthRow
    if 0 <= i < self.lengthRow or 0 <= j < self.lengthColumn:
        return True
    else:
        return False
```
Or
```python
def legalCoord(self, i, j):
    # lengthColumn, lengthRow
    return True if 0 <= i < self.lengthRow or 0 <= j < self.lengthColumn else False:
```
