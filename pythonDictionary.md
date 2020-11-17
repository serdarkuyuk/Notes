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

```Python
dic = {}
   for i, num in enumerate(arr):
       dic[num] = dic.get(num,0)+1
```


Forms a dictionary with key as a vowel and the value as 0
```python
vowels = 'aeiou'
count = {}.fromkeys(vowels, 0)
```
count = {'u': 0, 'o': 0, 'e': 0, 'a': 0, 'i': 0}
