# Python Generator function

first define a function with **yield**
Then call this function and assign to a variable
Then loop over and call each with **next** function
```python
def myGenerator(nums, n):
    for i in range(n):
        yield nums[i]
        yield nums[i+n]

generator = myGenerator(nums, n)
for _ in range(n*2):
    print(next(generator))
  ```
