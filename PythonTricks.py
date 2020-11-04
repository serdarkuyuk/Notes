# Run if list empty then do something else

```python
import bisect
res = []
for num in nums:                    #first run
    if not res or num > res[-1]: # if True or x : do not depend on x
        res.append(num)             #next run
    else:                        # if False or x : depend on x
        idx = bisect.bisect_left(res,num)
        res[idx] = num

print(len(res))

# or put the first number into list
result = [nums[0]]
for num in nums[1:]:
    if num > result[-1]:
        result.append(num)
    else:
        index = bisect_left(result, num)
        result[index] = num

return len(result)
```

#Two pointer example2

```python
g = [10,9,8,7]
s = [5,6,7,8]

g.sort()
s.sort()

i = j = 0
satisfied = 0
while i < len(g) and j < len(s):
    if g[i] <= s[j]:
        satisfied += 1
        j += 1
        i += 1
    else:
        j += 1
```

#Creating dictinary with list value

```python
pieces = [[78],[4,64],[91]]
myDictionary = {x[0]:x for x in pieces}
```

#Dictionary key value empty
get value from dictionary by asking key value, return empty list if there is no key value

'''python
myDictionary.get(i, [])
'''
