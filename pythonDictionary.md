# setdefault

```Python
myDict = {}
for num in nums:
    if num not in myDict:
        myDict.setdefault(num, 1)
    else:
        myDict[num] += 1
```

from collections import defaultdict
```python
counts = defaultdict(int)
for num in nums:
    counts[num] += 1
```
