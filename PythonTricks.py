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
```
